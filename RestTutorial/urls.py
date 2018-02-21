from django.conf.urls import include, url
from django.contrib import admin


from rest_framework import routers

urlpatterns = [
    # Examples:
    # url(r'^$', 'RestTutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^snip/', include('snippets.urls', namespace='snippets')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^blogpost/', include('blogpost.urls')),

]
