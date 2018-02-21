# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Post, Photo
from users.serializers import UserProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(many=False)
    photos = serializers.HyperlinkedIdentityField(view_name='postphoto-list')

    def get_validation_exclusions(self):
        # Need to exclude `author` since we'll add that later based off the request
        exclusions = super(PostSerializer, self).get_validation_exclusions()
        return exclusions + ['author']

    class Meta:
        model = Post
        #fields = ('title', 'body')
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')

    class Meta:
        model = Photo
        fields = "__all__"
