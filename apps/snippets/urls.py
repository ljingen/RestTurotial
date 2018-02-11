from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetail, UserList, UserDetail


urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
    url(r'^users/$', UserList.as_view(), name='my_user'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='my_profile'),
]