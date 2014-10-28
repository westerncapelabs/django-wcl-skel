FROM ubuntu:trusty

# Apt packages
RUN apt-get update
RUN apt-get install -y python python-pip
RUN apt-get install -y nginx
RUN apt-get install -y supervisor

# libpq needed for psycopg2
RUN apt-get install -y libpq-dev python-dev

# Mount the project
RUN mkdir -p /srv/wcl/{{cookiecutter.repo_name}}
RUN mkdir -p /var/log/wcl/{{cookiecutter.project_name}}

# Add local repo, and remove the Dockerfile for caching
ADD . /srv/wcl/{{cookiecutter.repo_name}}
RUN rm /srv/wcl/{{cookiecutter.repo_name}}/Dockerfile

# Python apps
RUN pip install -r /srv/wcl/{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}/requirements.txt

# nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN cp /srv/wcl/{{cookiecutter.repo_name}}/config/nginx/{{cookiecutter.project_name}}.conf /etc/nginx/sites-enabled/

# supervisord
RUN cp /srv/wcl/{{cookiecutter.repo_name}}/config/supervisord/supervisor.conf /etc/supervisor/conf.d/

#RUN /srv/wcl/{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}/manage.py migrate --noinput
RUN /srv/wcl/{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}/manage.py collectstatic --noinput

EXPOSE 80
CMD ["supervisord", "-n"]
