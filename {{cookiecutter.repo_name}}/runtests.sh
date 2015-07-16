#!/bin/sh
export DATABASE_URL='postgres://postgres:@/test_{{cookiecutter.project_name}}'
export DJANGO_SETTINGS_MODULE="{{cookiecutter.project_name}}.testsettings"
./manage.py test "$@"
