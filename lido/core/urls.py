from django.conf.urls import patterns, url

urlpatterns = patterns('lido.core.views',
    url(r'^$', 'index'),
)
