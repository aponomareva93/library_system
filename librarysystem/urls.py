from django.conf.urls import patterns, include, url
from django.contrib import admin
from books import views
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'librarysystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^search/$', views.search),
)
