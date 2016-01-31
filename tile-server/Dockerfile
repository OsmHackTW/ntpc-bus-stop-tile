FROM debian:jessie

RUN echo "deb http://httpredir.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y libmapnik2.2 mapnik-utils \
    fonts-noto-cjk libgeos-dev libgdal-dev libproj0 \
    python-pip python-imaging python-yaml python-shapely && \
    rm -rf /var/lib/apt/lists/*
RUN pip install MapProxy==1.8.1
