from django.conf.urls import url, include
from rest_framework import routers
from django.urls import include, path
from django.contrib import admin
from web.views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'placeholders', PlaceholderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'axon'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('web/', include('web.urls')),
    path('admin/', admin.site.urls),
]