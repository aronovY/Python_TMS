from django.contrib.auth.models import User
from django.test import TestCase, Client

from dashboard.models import Issue, Project


class TestUpdateIssue(TestCase):

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

    def test_should_return_true_on_successful_update_issue(self):
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
        print(f'Name: {test_issue.name}\nDescription: {test_issue.description}\n'
              f'Created_at: {test_issue.created_at}\nDeadline: {test_issue.deadline}\n'
              f'Assigne: {test_issue.assigne}\nProject: {test_issue.project}\n'
              f'Reported: {test_issue.reported}')
        new_name = 'New Issue'
        new_description = 'New description'
        new_deadline = '2020-09-10'
        response = self.http_client.post(
            f'/issue/{test_issue.id}/update/',
            {
                'name': new_name,
                'description': new_description,
                'deadline': new_deadline,
                'assigne': self.user.id,
                'project': self.project.id,
                'reported': self.user.id
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Issue.objects.filter(name=new_name).values_list('name', flat=True).first(),
            new_name
        )