/* Execute using: 
    psql -U dba -W -d dvdrental -a -f structure.sql
    or
    \i \path\structure.sql 
    inside psql  
    Check https://gist.github.com/MercadoMR/d0c394e57c06eda16cb4e1e634fab9bf for more information
*/

CREATE SCHEMA rentals;

CREATE TABLE rentals.film (
   id_dvd SERIAL PRIMARY KEY,
   title VARCHAR(255) NOT NULL,
   film_description TEXT,
   film_length INTERVAL
);

INSERT INTO rentals.film (title, film_description)
VALUES
    ('Godzilla vs King Kong', 'Le monkey vs Le Lizard.\n An interesting movie where Godzilla returns as...'),
    ('Interstelar', 'A beautiful film where various types of topics are reviewed, for example...');
