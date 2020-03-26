from django.contrib.auth import models

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            # initial
            'id',
            'url',
            'username',
            'first_name',
            'last_name',
            'date_joined',
            'last_login',

            # second phase
            'groups',
        )
        read_only_fields = (
            'date_joined',
            'last_login',
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = (
            'url',
            'name',
        )