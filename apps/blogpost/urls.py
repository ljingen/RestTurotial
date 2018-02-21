from django.conf.urls import url
from blogpost.views import PostList, PostDetail, PhotoList, PhotoDetail,UserPostList,PostPhotoList


urlpatterns = [
    url(r'^posts/$', PostList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>\d+)$', PostDetail.as_view(), name='post-detail'),
    url(r'^posts/(?P<pk>\d+)/photos$', PostPhotoList.as_view(), name='postphoto-list'),

    url(r'^photos/$', PhotoList.as_view(), name='photo-list'),
    url(r'^/(?P<pk>\d+)$', PhotoDetail.as_view(), name='photo-detail'),
]
