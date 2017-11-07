"""cshc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls.static import static
from graphene_django.views import GraphQLView

from .views import HomeView
from members.views import ProfileView

#pylint: disable=C0103
urlpatterns = [
    # The main landing page
    url(r'^$', HomeView.as_view(), name='homepage'),

    # Stats landing page
    url(r'^stats/$', TemplateView.as_view(template_name='core/stats.html'), name='stats'),

    url(r'^matches/', include('matches.urls')),
    url(r'^opposition/', include('opposition.urls')),
    url(r'^venues/', include('venues.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^teams/', include('teams.urls')),
    url(r'^training/', include('training.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),  # CKEditor Urls
    url(r'^accounts/profile/$', ProfileView.as_view(), name='user_profile'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),   # GraphQL Urls
    url(r'^admin/', admin.site.urls),
] + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
