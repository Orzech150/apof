from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='login', email='test@test.pl', password='P@ssw0rd!'
        )

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            isinstance(response.context['form'], AuthenticationForm)
        )

        form_data = {'username': 'login', 'password': 'wrong_password'}
        response = self.client.post(reverse('login'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['form'].errors['__all__'],
            [
                'Please enter a correct username and password. '
                'Note that both fields may be case-sensitive.'
            ]
        )
        form_data['password'] = 'P@ssw0rd!'
        response = self.client.post(reverse('login'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
