from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from coordi.settings import MEDIA_URL, MEDIA_ROOT
from coordi.base.views import custom_login, custom_logout, \
main, how_it_works, signup, signup_thanks
from coordi.showcase.views import showcase, redirect_showcase, album
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coordi.views.home', name='home'),
    # url(r'^coordi/', include('coordi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', signup),
    url(r'^signup/thanks/$', signup_thanks),
    url(r'^login/$',  custom_login),
    url(r'^logout/$', custom_logout),

    url(r'^$', main),
    url(r'^info/how_it_works/$', how_it_works),
    url(r'^showcase/$', redirect_showcase),

    url(r'^showcase/([1-9][0-9]*)/$', showcase),
    url(r'^showcase/album/(.*)/$', album),

)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()