from django.contrib.auth.models import User
from django.test import TestCase, Client

from dashboard.models import Issue, Project


class TestReadIssue(TestCase):

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

    def test_should_return_true_on_successful_read_project(self):
        # Issue
        self.name_issue = 'Test issue'
        self.issue = Issue.objects.create(
            name=self.name_issue,
            description='Description about test issue',
            deadline='2020-05-12',
            assigne=User.objects.get(id=1),
            project=Project.objects.get(id=1),
            reported=User.objects.get(id=1)
        )
        self.http_client.login(username=self.username, password=self.user_password)
        test_issue = Issue.objects.get(name=self.name_issue)
        response = self.http_client.get(f'/issue/{test_issue.id}/')
        self.assertEqual(response.status_code, 200)

