-- Creates the database hbtn_0d_usa and the table states
-- Database will contain a table of states with unique IDs and names
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    name VARCHAR(256) NOT NULL
);
