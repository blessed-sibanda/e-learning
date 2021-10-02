FROM ubuntu:18.04

# add code and directories
RUN mkdir /elearning
WORKDIR /elearning
COPY requirements.txt /elearning/
COPY django/ /elearning/django
COPY scripts/ /elearning/scripts
RUN mkdir /var/log/elearning/
RUN touch /var/log/elearning/elearning.log

# install packages
RUN apt-get -y update 
RUN apt-get install -y \   
    nginx-core \
    nginx \
    iproute2 \
    libnginx-mod-http-geoip \
    postgresql-client \
    python3.8 \
    python3-pip 

# install pip dependencies
RUN pip3 install virtualenv
RUN virtualenv /elearning/venv
RUN bash /elearning/scripts/pip_install.sh /elearning

# collect static files 
RUN bash /elearning/scripts/collect_static.sh /elearning

WORKDIR /elearning/django 
CMD python manage.py collectstatic

WORKDIR /elearning

# nginx
COPY nginx/elearning.conf /etc/nginx/sites-available/elearning.conf
RUN rm /etc/nginx/sites-enabled/*
RUN ln -s /etc/nginx/sites-available/elearning.conf /etc/nginx/sites-enabled/elearning.conf

COPY runit/nginx /etc/service/nginx 
RUN chmod +x /etc/service/nginx/run

# configure uwsgi
COPY uwsgi/elearning.ini /etc/uwsgi/apps-enabled/elearning.ini 
RUN mkdir -p /var/log/uwsgi/
RUN touch /var/log/uwsgi/elearning.log 
RUN chown www-data /var/log/uwsgi/elearning.log 
RUN chown www-data /var/log/elearning/elearning.log 

COPY runit/uwsgi /etc/service/uwsgi 
RUN chmod +x /etc/service/uwsgi/run

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80