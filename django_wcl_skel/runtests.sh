#!/bin/sh
export DATABASE_URL='postgres://postgres:@/test_django_wcl_skel'
export DJANGO_SETTINGS_MODULE="django_wcl_skel.testsettings"
./manage.py test "$@"