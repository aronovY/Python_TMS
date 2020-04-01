from django.contrib.auth.models import User

from django.test import TestCase, Client

from dashboard.models import Issue, Project


class TestCreateIssue(TestCase):

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

        # Project
        self.name_project = 'Test project'
        self.project = Project.objects.create(
            name=self.name_project,
            description='Description about test project'
        )

    def test_should_return_true_on_successful_create_issue(self):
        self.http_client.login(username=self.username, password=self.user_password)
        test_issue_name = 'Test_issue'
        # Get user and project
        usr = User.objects.get(username='dummy')
        prj = Project.objects.get(name='Test project')
        response = self.http_client.post(
            '/issue/create/', {'name': test_issue_name,
                               'description': 'Test description',
                               'deadline': '2020-05-12',
                               'assigne': usr.id,
                               'project': prj.id,
                               'reported': usr.id

                              }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Issue.objects.filter(name=test_issue_name).values_list('name', flat=True).first(),
            test_issue_name
        )
