# Sproner
This is an example using Spring + Hibernate + Postgres to make a RESTful API. \
My intention here is to create the end-point of a music service. \
In the next table are described the Methods, URLs and their corresponding actions:

| Method | URL | Action |
| ------ | --- | ------ |
| _POST_ | **/api/song** | Create a new song |
| _GET_ | **/api/song** | Retrieve all songs |
| _DELETE_ | **/api/song** | Delete all songs |
| _GET_ | **/api/song/<id>** | Retrieve a song by id |
| _PUT_ | **/api/song/<id>** | Update a song by id |
| _DELETE_ | **/api/film/<id>** | Delete a song by id |

## Setting the database

Before doing anything is needed to create the database for our project and grant permissions on it. \
For this I'll run the following command inside psql, on an superuser account:
```
CREATE TABLESPACE sproner_music 
OWNER 'dba'
LOCATION 'C:\pdbs\sproner';

CREATE DATABASE musiclibrary
WITH 
ENCODING='UTF8' 
OWNER='dba'
TABLESPACE='sproner_music';

GRANT ALL PRIVILEGES
ON DATABASE musiclibrary
TO dba;
```

As I said it's required to run the previous command on a superuser account. For example using: \
```
psql -U postgres -W -d postgres -a -f structure.sql
```
Then I'll create two schemas: \
```
/* Inside the musiclibrary database (psql -U dba -W -d musiclibrary) */
CREATE SCHEMA music;
CREATE SCHEMA users;
SET search_path TO music, users , public;
```
