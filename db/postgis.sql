CREATE EXTENSION postgis;

CREATE TABLE ntpc_stops (
  "name" character varying(255),
  "location" geometry(POINT, 4326),
  "route" character varying(255),
  "direction" smallint
);

CREATE INDEX name_idx ON ntpc_stops USING BTREE ("name");
CREATE INDEX location_idx ON ntpc_stops USING GIST ("location");

CREATE TABLE ntpc_stop_group (
  "name" character varying(255),
  "convex_hull" geometry
)
