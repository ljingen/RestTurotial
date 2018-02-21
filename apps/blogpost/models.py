from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Post(models.Model):
    """
    帖子
    """
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(u'标题', max_length=255)
    body = models.TextField(u'文章', blank=True, null=True)


class Photo(models.Model):
    """
    图片
    """
    post = models.ForeignKey(Post, related_name='photos', verbose_name='文章')
    image = models.ImageField(u'图片', upload_to="images/%Y/%m/%d")
