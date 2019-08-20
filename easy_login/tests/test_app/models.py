# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.db import models
# from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)
# from django.utils import timezone


# class UserManager(BaseUserManager):
#     def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
#         now = timezone.now()
#         if not email:
#             raise ValueError('users must have an email address')
#         email = self.normalize_email(email)
#         user = self.model(email = email,
#                             is_staff = is_staff,
#                             is_superuser = is_superuser,
#                             last_login = now,
#                             date_joined = now,
#                             **extra_fields)
#         user.set_password(password)
#         user.save(using = self._db)
#         return user
#
#     def create_user(self, email, password=None, **extra_fields):
#         user = self._create_user(email, password, False, False, **extra_fields)
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         user = self._create_user(email, password, True, True, **extra_fields)
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     """My own custom user class"""
#
#     email = models.EmailField(max_length=255, unique=True, db_index=True, verbose_name='email address')
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = UserManager()
#
#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
#
#     def get_full_name(self):
#         """Return the email."""
#         return self.email
#
#     def get_short_name(self):
#         """Return the email."""
#         return self.email
