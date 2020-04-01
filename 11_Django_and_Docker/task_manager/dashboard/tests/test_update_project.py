from django.contrib.auth.models import User
from django.test import TestCase, Client

from dashboard.models import Project


class TestUpdateProject(TestCase):

    def setUp(self) -> None:
        # User created for login
        self.user_password = 'dummy_pass'
        self.username = 'dummy'
        self.user = User.objects.create(
            username=self.username,
            is_active=True
        )
        self.http_client = Client()
        self.user.set_password(self.user_password)
        self.user.save()

        # Project
        self.name_project = 'Test project'
        self.project = Project.objects.create(
            name=self.name_project,
            description='Description about test project'
        )

    def test_should_return_true_on_successful_update_project(self):
        self.http_client.login(username=self.username, password=self.user_password)
        test_project = Project.objects.get(name=self.name_project)
        print(f'Name: {test_project.name}\nDescription: {test_project.description}')
        new_name = 'New Test'
        new_description = 'New description'
        response = self.http_client.post(
            f'/projects/{test_project.id}/update/',
            {
                'name': new_name,
                'description': new_description
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Project.objects.filter(name=new_name).values_list('name', flat=True).first(),
            new_name
        )