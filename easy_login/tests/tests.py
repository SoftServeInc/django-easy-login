# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase, Client
from bs4 import BeautifulSoup
from django.urls import reverse_lazy

from easy_login.context_processors import easy_login

import re


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', )

    username = 'Admin'
    email = 'user@adm.com'


class EasyLoginTest(TestCase):
    def setUp(self):
        self.admin_password = "admin"

        admin = UserFactory(is_staff=True, is_superuser=True)
        admin.set_password(self.admin_password)
        admin.save()

        user_1 = UserFactory(username='User_1')
        user_1.set_password('user1')
        user_1.save()

        user_2 = UserFactory(username='User_2')
        user_2.set_password('user2')
        user_2.save()

        user_3 = UserFactory(username='User_3')
        user_3.set_password('user3')
        user_3.save()

    def test_user_list_view(self):
        request_factory = RequestFactory()
        request = request_factory.get(reverse_lazy('test-app:index'))
        request.user = User.objects.get(username='Admin')
        response = easy_login(request)
        soup = BeautifulSoup(response['easy_login'], features="html.parser")
        user_name_obj = soup.find('select', {'id': 'id_user_name'})
        user_real_set = set(User.objects.all().values_list('username', flat=True))
        user_new_set = {user_obj.text for user_obj in user_name_obj.find_all('option') if user_obj['value']}
        self.assertEqual(user_new_set, user_real_set)

    def test_current_user(self):
        request_factory = RequestFactory()
        request = request_factory.get(reverse_lazy('test-app:index'))
        for user in User.objects.all():
            request.user = user
            response = easy_login(request)
            soup = BeautifulSoup(response['easy_login'], features="html.parser")
            search_compile = re.compile('Current User: (.*) - ID:.*')
            user_name = soup.find('span', text=search_compile)
            user_name = re.findall(search_compile, user_name.text)[0] if user_name else None
            self.assertEqual(request.user.username, user_name)

    def test_form(self):
        client = Client()

        admin = User.objects.get(username='Admin')
        client.login(username=admin.username, password=self.admin_password)

        response = client.get(reverse_lazy('test-app:index'))
        soup = BeautifulSoup(response.content, features="html.parser")
        search_compile = re.compile('Current User: (.*) - ID:.*')
        user_name = soup.find('span', text=search_compile)
        user_name = re.findall(search_compile, user_name.text)[0] if user_name else None
        self.assertEqual(admin.username, user_name)

        user_1 = User.objects.get(username='User_1')
        client.post(
            reverse_lazy('easy-login:easy-login-change'),
            {
                'user_name': '',
                'user_id': user_1.id
            }
        )

        response = client.get(reverse_lazy('test-app:index'))
        soup = BeautifulSoup(response.content, features="html.parser")
        search_compile = re.compile('Current User: (.*) - ID:.*')
        user_name = soup.find('span', text=search_compile)
        user_name = re.findall(search_compile, user_name.text)[0] if user_name else None

        self.assertEqual(user_1.username, user_name)

        client.post(
            reverse_lazy('easy-login:easy-login-change'),
            {
                'user_name': admin.id,
                'user_id': ''
            }
        )

        response = client.get(reverse_lazy('test-app:index'))
        soup = BeautifulSoup(response.content, features="html.parser")
        search_compile = re.compile('Current User: (.*) - ID:.*')
        user_name = soup.find('span', text=search_compile)
        user_name = re.findall(search_compile, user_name.text)[0] if user_name else None

        self.assertEqual(admin.username, user_name)
