from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase, Client

User = get_user_model()


class TestSignInRegister(TestCase):

    def setUp(self) -> None:
        self.user_password = 'dummy_pass'
        self.username = 'dummy'
        self.user = User.objects.create(
            username=self.username,
            # password=User.set_password(self.user_password),
            is_active=True
        )
        self.http_client = Client()
        self.user.set_password(self.user_password)
        self.user.save()

    def test_should_return_true_on_successful_login(self):
        is_logged = self.http_client.login(username=self.username, password=self.user_password)
        self.assertTrue(is_logged)
        # breakpoint()

    def test_should_return_true_on_successful_register(self):
        test_username = 'Antoshka'
        response = self.http_client.post(
            '/register/', {'username': test_username,
                           'password1': 'qwerty1010',
                           'password2': 'qwerty1010',
                           'email': 'user@user.com',
                           'first_name': 'Vasya',
                           'last_name': 'Ivanov'
                           }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            User.objects.filter(username=test_username).values_list('username', flat=True).first(),
            test_username
        )
        # breakpoint()