-- Create database and table
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use new database
USE hbtn_0d_usa;
-- Create new table in new database
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL UNIQUE AUTO_INCREMENT,
	name VARCHAR(256),
	PRIMARY KEY(id));
