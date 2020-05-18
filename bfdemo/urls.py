from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'nplusone/$', views.nplusone, name='nplusone'),
    url(r'memspike/$', views.memspike, name='memspike'),
]
