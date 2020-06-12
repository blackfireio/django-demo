from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'nplusone/$', views.nplusone, name='nplusone'),
    #url(r'nplusone-fix/$', views.nplusone_fix, name='nplusone-fix'),
    url(r'memspike/$', views.memspike, name='memspike'),
    url(r'dummy/$', views.dummy, name='dummy'),
    #url(r'memspike-fix/$', views.memspike_fix, name='memspike-fix'),
]
