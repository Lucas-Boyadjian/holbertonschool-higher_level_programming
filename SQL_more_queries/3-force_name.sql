-- Script that creates the table force_name
-- The table contains an id field (integer) and a name field (string) that cannot be null
CREATE TABLE IF NOT EXISTS force_name (
    id INT, 
    name VARCHAR(256) NOT NULL
);
