from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'nplusone/$', views.nplusone, name='nplusone'),
    url(r'nplusone-fix/$', views.nplusone_fix, name='nplusone-fix'),
    url(r'memspike/$', views.memspike, name='memspike'),
    url(r'memspike-fix/$', views.memspike_fix, name='memspike-fix'),
    url(r'load-me/$', views.load_me, name='load-me'),
    url(r'apm-autoprofile/$', views.apm_autoprofile, name='apm-autoprofile'),
    url(r'allinone/$', views.AllInOneView.as_view(), name='allinone'),
]
