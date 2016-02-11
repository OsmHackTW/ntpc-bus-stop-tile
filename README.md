# ntpc-bus-stop-tile

A total solution tile generator using Docker Compose,
for generating tile from New Taipei City bus stops data.

Database:

* PostgreSQL 9.5
* PostGIS 2.2
* Python

Tile server:

* CartoCSS (thus Node.js)
* Mapnik
* MapProxy
* uWSGI

## Installation

For Linux, install recent version of Docker and Docker Compose.

Run `docker-compose up` to build Docker images and lanuch both
the database and tile container.

Now, open another terminal, run the following command to import stops:

    docker-compose run db python /process.py

It may take several minutes, so be patient :)

Now a WMTS server will be ready at port `8888`. You can append an entry
in JOSM like the following to get started:

    wmts:http://127.0.0.1:8888/wmts/1.0.0/WMTSCapabilities.xml

--------------------

For Windows or Mac user, you can install Docker Toolbox from Docker
official website, and use Docker Quickstart Terminal to execute same
commands. Remember you should change the IP address to the Docker Machine
IP, like replace `127.0.0.1` to `192.168.99.100`.
