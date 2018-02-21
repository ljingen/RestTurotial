from django.contrib import admin
from blogpost.models import Post, Photo


class PostAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'body')


class PhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Photo, PhotoAdmin)
