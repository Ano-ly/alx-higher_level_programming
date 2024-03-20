-- Create table with unique id
-- Create table
CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256));
