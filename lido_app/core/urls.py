from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.views import logout

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', logout, kwargs={'next_page': '/'}, name='logout')
)
