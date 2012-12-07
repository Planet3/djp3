from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'horseshoe.views.home', name='home'),
    # url(r'^horseshoe/', include('horseshoe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': '/home/mtobis/webapps/djp3/addons/tinymce/jscripts/tiny_mce/' }),
    (r'', include('django.contrib.flatpages.urls')),
)
