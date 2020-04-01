from django import urls
from django.db import models

from django.conf import settings


class Project(models.Model):
    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        max_length=1000
    )
    created_at = models.DateField(
        auto_now=True
    )
    users_project = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='users_project'
    )

    def get_absolute_url(self):
        return urls.reverse('projects-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.name)


class Issue(models.Model):
    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        max_length=2000
    )
    created_at = models.DateTimeField(
        auto_now=True
    )
    reported = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='reporters'
    )
    assigne = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigns'
    )
    deadline = models.DateField(
        null=False,
        blank=False
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project'
    )

    def get_absolute_url(self):
        return urls.reverse('issue-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.name)


class Files(models.Model):
    id_issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,)
    file_link = models.FileField(
        upload_to='logos',
        null=True,
        blank=True)
