from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'comments/$', views.comments, name='comments'),
    url(r'generate/$', views.generate, name='generate'),
]
