from django.conf.urls import patterns, include, url
from django.contrib import admin

from readers import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'librarysystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'books.views.search', name='search'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^index/$', 'librarysystem.views.index', name='index'),
    url(r'^homepage/$', views.home)
)
