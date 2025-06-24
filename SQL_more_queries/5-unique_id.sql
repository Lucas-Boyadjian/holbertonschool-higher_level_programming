-- Script that creates the table unique_id
-- The table contains an id field (integer) with default value 1 and UNIQUE constraint
-- Also contains a name field (string)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE, 
    name VARCHAR(256)
);
