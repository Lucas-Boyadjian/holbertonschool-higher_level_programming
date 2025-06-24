-- Script that creates the table id_not_null
-- The table contains an id field (integer) with default value 1 and a name field (string)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1, 
    name VARCHAR(256)
);
