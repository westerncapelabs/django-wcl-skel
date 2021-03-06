import os
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = os.environ.get('{{cookiecutter.env_prefix}}_TITLE', '{{cookiecutter.project_name}} Admin')


urlpatterns = patterns(
    '',
    url(r'^admin/',  include(admin.site.urls)),
    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/token-auth/',
        'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^', include('{{cookiecutter.app_name}}.urls')),
)
