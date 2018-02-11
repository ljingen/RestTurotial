#-*- coding:utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    对User进行Serializer 序列化
    """


    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'is_staff')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    对Group这个 model进行serializers序列化
    """


    class Meta:
        model = Group
        fields = ('url', 'name')
