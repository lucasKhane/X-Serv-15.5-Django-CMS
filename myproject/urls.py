from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index\.html$', 'cms.views.index'),
    url(r'^pages/nuevorecurso/(.*)/(.*)', 'cms.views.nuevorecurso'),
    url(r'^pages/(\d+)', 'cms.views.recurso'),
    url(r'^.*', 'cms.views.el404'),
)
