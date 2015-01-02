from fabric.api import cd, sudo, env
import os

PROJECT = '{{cookiecutter.repo_name}}'
DJANGO = '{{cookiecutter.project_name}}'
USER = ''

env.path = os.path.join('/srv', 'wcl', PROJECT)
env.django = os.path.join('/srv', 'wcl', PROJECT, DJANGO)
env.venv = os.path.join('/srv', 'wcl', 'python', PROJECT)


def restart():
    sudo('/etc/init.d/nginx restart')
    sudo('supervisorctl reload')


def deploy():
    with cd(env.path):
        sudo('git pull', user=USER)

    with cd(env.django):
        sudo(env.venv + '/bin/python manage.py syncdb --noinput',
             user=USER)
        sudo(env.venv + '/bin/python manage.py collectstatic --noinput',
             user=USER)


def install_packages(force=False):
    with cd(env.django):
        sudo(env.venv + '/bin/pip install %s -r requirements.txt' % (
             '--upgrade' if force else '',), user=USER)
