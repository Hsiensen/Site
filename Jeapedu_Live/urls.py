from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Jeapedu_Live.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'Jeapedu_Live.views.index', name='index'),
    url(r'^courses$', 'Jeapedu_Live.views.courses', name='courses'),
    url(r'^student$', 'Jeapedu_Live.views.student', name='student'),
    url(r'^taped$', 'Jeapedu_Live.views.taped', name='taped'),
    url(r'^live$', 'Jeapedu_Live.views.live', name='live'),
    url(r'^ready$', 'Jeapedu_Live.views.ready', name='ready'),

    url(r'^admin/', include(admin.site.urls)),
)
