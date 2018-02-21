# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):

    posts = serializers.HyperlinkedIdentityField(view_name="users:userpost-list", lookup_field="username")

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
