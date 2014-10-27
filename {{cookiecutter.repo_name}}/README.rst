{{cookiecutter.repo_name}}
=======================================

Setup
---------------------------------------

Remember to enable hbase on your postgres template
::
    psql -d template1 -c 'create extension hstore;'
