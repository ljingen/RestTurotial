from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户个人资料
    """
    followers = models.ManyToManyField('self', related_name='followees', symmetrical=False, default=None)
    name = models.CharField(u'姓名', max_length=30, null=True, blank=True)
    birthday = models.DateField(u'生日', null=True, blank=True)
    mobile = models.CharField(u'电话', max_length=11, null=True, blank=True)
    gender = models.CharField(choices=(('male', u'男'), ('female', u'女')), default='male', max_length=6)
    email = models.CharField(u'邮箱', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户管理'

    def __str__(self):
        return self.name if self.name else self.username
