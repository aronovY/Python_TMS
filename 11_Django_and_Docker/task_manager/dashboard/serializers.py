from rest_framework import serializers

from dashboard import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = (
            'id',
            'url',
            'name',
            'description',
            'created_at',
            'users_project'
        )

        read_only_fields = (
            'created_at',
            'users_project',
        )


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue
        fields = (
            'id',
            'url',
            'name',
            'description',
            'created_at',
            'reported',
            'assigne',
            'deadline',
            'project')

        read_only_fields = (
            'created_at',
            'reported',
            'assigne',
            'deadline'
        )


