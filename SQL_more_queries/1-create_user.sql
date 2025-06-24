-- Script that creates the MySQL server user user_0d_1 with all privileges
-- Creates the user if it doesn't exist already with password 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants all privileges on all databases and tables to this user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
