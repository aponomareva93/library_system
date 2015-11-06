from django.conf.urls import patterns, include, url
from django.contrib import admin

from readers import forms


admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'librarysystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'books.views.search', name='search'),
    url(r'^login/$', forms.LoginFormView.as_view()),
    url(r'^logout/$', forms.LogoutView.as_view()),
    url(r'^index/$', 'librarysystem.views.index', name='index'),
    url(r'^$', 'librarysystem.views.index', name='index'),
    url(r'^change_pass/$', 'readers.views.change_password', name='change_password'),
)
