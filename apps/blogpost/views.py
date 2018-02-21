from rest_framework import generics
from blogpost.models import Post, Photo
from blogpost.serializers import PostSerializer, PhotoSerializer
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserPostList(generics.ListAPIView):
    """
    根据username 获取这个user的所有post
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        """
        Get the list of items for this view.
        """
        queryset = Post.objects.all().filter(author__username=self.kwargs.get('username'))

        return queryset


class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDetail(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PostPhotoList(generics.ListAPIView):
    """
    根据post,获取当前post下的photo
    """
    serializer_class = PhotoSerializer

    def get_queryset(self):
        """
        Get the list of items for this view.
        """
        queryset = Photo.objects.all().filter(post__pk=self.kwargs.get('pk'))
        return queryset
