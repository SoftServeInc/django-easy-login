# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase, Client
from bs4 import BeautifulSoup
from easy_login.context_processors import easy_login

import re


class EasyLoginTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.admin = User.objects.create_user(
            username='Admin',
            password='admin',
            email='admin@adm.com',
            is_superuser=True,
            is_staff=True
        )
        self.user_1 = User.objects.create_user(
            username='User_1',
            password='user1',
            email='user1@adm.com'
        )
        self.user_2 = User.objects.create_user(
            username='User_2',
            password='user2',
            email='user2@adm.com'
        )
        self.user_3 = User.objects.create_user(
            username='User_3 long name test',
            password='user3',
            email='user3@adm.com'
        )

    def test_user_list_view(self):
        request = self.factory.get('/')
        request.user = self.admin
        response = easy_login(request)
        with open('template.html', 'w') as ff:
            ff.write(response['easy_login'])
        soup = BeautifulSoup(response['easy_login'], features="html.parser")
        user_name_obj = soup.find('select', {'id': 'id_user_name'})
        user_real_list = set(User.objects.all().values_list('username', flat=True))
        user_new_list = {user_obj.text for user_obj in user_name_obj.find_all('option') if user_obj['value']}
        self.assertEqual(user_new_list, user_real_list)

    def test_current_user(self):
        request = self.factory.get('/')
        for user in [self.admin, self.user_1, self.user_2, self.user_3]:
            request.user = user
            response = easy_login(request)
            soup = BeautifulSoup(response['easy_login'], features="html.parser")
            search_compile = re.compile('Current User: (.*) - ID:.*')
            user_name = soup.find('p', text=search_compile)
            user_name = re.findall(search_compile, user_name.text)[0] if user_name else None
            self.assertEqual(request.user.username, user_name)

    def test_form(self):
        client = Client()
        client.login(username='Admin', password='admin')
        response = client.post(
            '/easy_login/easy_login_change/',
            {
                'user_name': self.user_1.id,
                'user_id': ''
            }
        )

        print(response.cookies)

        print(response)
        print(response.content)
        self.assertTrue(True)
