from django.conf.urls import include, url
from django.contrib import admin


from rest_framework import routers
from quickstart import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'/users', views.UserViewSet)
router.register(r'/group', views.GroupViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'RestTutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test', include(router.urls)),
    url(r'^snip/', include('snippets.urls', namespace='snippets')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
