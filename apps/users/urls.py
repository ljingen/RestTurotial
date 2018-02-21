from django.conf.urls import url

from users.views import UserList, UserDetail
from blogpost.views import UserPostList


urlpatterns = [
    url(r'^$', UserList.as_view(), name='user-list'),
    url(r'^(?P<username>[0-9a-zA-Z_-]+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
]
