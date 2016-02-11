FROM postgres:9.5
RUN apt-get update && \
    apt-get install -y postgresql-9.5-postgis-2.2 postgis python-requests python-psycopg2 python-unicodecsv && \
    rm -rf /var/lib/apt/lists/*
ADD ./postgis.sql /docker-entrypoint-initdb.d
ADD ./process.py /process.py
