from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^download/.*$', 'django_transfer.views.download', name='download'),
    url(r'^upload/$', 'django_transfer.views.upload', name='upload'),
)
