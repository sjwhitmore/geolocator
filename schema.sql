drop table if exists locations;
create table locations (
  id integer primary key autoincrement,
  sid text not null,
  date text not null,
  visitor_lat text not null,
  visitor_long text not null,
  visitor_city text not null,
  visitor_region text not null,
  visitor_country text not null,
  visitor_countrycode text not null
);