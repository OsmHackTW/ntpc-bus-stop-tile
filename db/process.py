import re
import sys
from cStringIO import StringIO
from zipfile import ZipFile
import psycopg2
import unicodecsv
import requests


def write_data(csvfile, conn):
    reader = unicodecsv.DictReader(csvfile)
    count = 0
    with conn.cursor() as cur:
        for row in reader:
            cur.execute(
                "INSERT INTO ntpc_stops"
                "(name, location, route, direction)"
                "VALUES (%s, ST_SetSRID(ST_MakePoint(%s, %s), 4326), %s, %s);",
                (row["Station_nameZh"], row["Station_longitude"],
                 row["Station_latitude"], row["Route_nameZh"],
                 row["Station_goBack"]))
            count += 1
        print "%d stops added" % count
        print "Calculating groups..."
        cur.execute(
            "INSERT INTO ntpc_stop_group (convex_hull, name) "
            "SELECT ST_ConvexHull(unnest(ST_ClusterWithin(ST_Buffer("
            "location, 0.0003), 0.001))), "
            "name from ntpc_stops GROUP BY name;"
        )
    print "OK"


NTPC = 'http://data.ntpc.gov.tw'

print "Parsing data page..."
data_text = requests.get(NTPC + '/od/detail?'
                         'oid=18621BF3-6B00-4A07-B49C-0C5CCABFE026').text
zip_url = re.search(r'\/od\/zipfile[^\"]+', data_text).group(0)

print "Getting ZIP file..."
zip_content = requests.get(NTPC + zip_url).content

print "Extracting..."
with ZipFile(StringIO(zip_content), "r") as zip_file:
    with zip_file.open(zip_file.infolist()[0].filename) as csvfile, \
         psycopg2.connect(dbname="postgres", user="postgres", host="db") \
         as conn:
        print "Writing..."
        write_data(csvfile, conn)
