# -*- coding:utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES,STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
#     """
#     第一种:直接继承Serializer，然后把每个变量都实现一次，把创建和更新也调整一下
#     """
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(required = False, allow_blank = True, max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     lineos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


class SnippetSerializer(serializers.ModelSerializer):
    """
    第二种:我们直接继承ModelSerializer，这样就不用写上面那些东西，直接写model = Snippet
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        #field = ('title', 'code', 'linenos', 'language', 'style')
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style','owner')

class UserSerializer(serializers.ModelSerializer):
    """
    实现User的序列化的序列器,直接使用serializers.ModelSerializer
    """
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    """
    snippets是因为我们在前面的Snippet的 model里面，定义了一个User的外键，并添加related_name = snippets
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')