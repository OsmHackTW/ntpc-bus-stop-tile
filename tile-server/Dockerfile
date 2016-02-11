FROM debian:jessie

RUN sed -i 's/httpredir/ftp.tw/g' /etc/apt/sources.list
RUN echo "deb http://ftp.tw.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y libmapnik2.2 mapnik-utils \
    fonts-noto-cjk libgeos-dev libgdal-dev libproj0 \
    python-pip python-imaging python-yaml python-shapely \
    nodejs-legacy npm uwsgi uwsgi-plugin-python && \
    rm -rf /var/lib/apt/lists/*
RUN pip install MapProxy==1.8.1
RUN npm install -g carto
ADD project.mml /
ADD mapproxy.yaml /
ADD style.mss /
ADD wsgi.py /
ADD uwsgi.ini /
RUN carto /project.mml > /mapnik.xml
CMD uwsgi /uwsgi.ini
