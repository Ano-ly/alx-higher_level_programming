-- Create new database and table
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use new database
USE hbtn_0d_usa;
-- Create new table in new database
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY (id),
	FOREIGN KEY (state_id)
	REFERENCES states(id));
