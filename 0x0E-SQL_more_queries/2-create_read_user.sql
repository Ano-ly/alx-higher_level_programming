-- Create new database, new user, grant user select priviledges on new database
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create new user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant priviledges to new user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
