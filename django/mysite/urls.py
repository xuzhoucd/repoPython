#

from django.conf.urls import include, url
from django.contrib import admin

from nine import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/extract$', views.extract_show),
    url(r'^admin/', include(admin.site.urls)),
]
