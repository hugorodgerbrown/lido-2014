# main project URL definitions.

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout

admin.autodiscover()

urlpatterns = patterns('',
    url('', include('lido.core.urls', namespace='core')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', logout, kwargs={'next_page': '/'}, name='logout')
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )