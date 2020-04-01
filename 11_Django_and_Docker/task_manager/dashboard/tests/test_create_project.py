from django.contrib.auth.models import User

from django.test import TestCase, Client

from dashboard.models import Project


class TestCreateProject(TestCase):

    def setUp(self) -> None:
        self.user_password = 'dummy_pass'
        self.username = 'dummy'
        self.user = User.objects.create(
            username=self.username,
            is_active=True
        )
        self.http_client = Client()
        self.user.set_password(self.user_password)
        self.user.save()

    def test_should_return_true_on_successful_create_project(self):
        self.http_client.login(username=self.username, password=self.user_password)
        test_project_name = 'Test_project'
        response = self.http_client.post(
            '/projects/create/', {'name': test_project_name,
                                  'description': 'Test description'
                                  }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Project.objects.filter(name=test_project_name).values_list('name', flat=True).first(),
            test_project_name
        )
