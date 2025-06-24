-- Script that creates the database hbtn_0d_2 and the user user_0d_2
-- Creates the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates the user if it doesn't exist with password 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants SELECT privilege on the hbtn_0d_2 database to this user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
