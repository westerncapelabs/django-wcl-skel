from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = os.environ.get('{{cookiecutter.env_prefix}}_TITLE', '{{cookiecutter.project_name}} Admin')


urlpatterns = patterns(
    '',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/',  include(admin.site.urls)),
    url(r'^{{cookiecutter.app_name}}/',
        include('{{cookiecutter.app_name}}.urls')),
)
