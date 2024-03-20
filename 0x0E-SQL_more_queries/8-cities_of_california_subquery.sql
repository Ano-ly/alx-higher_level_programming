-- Select from two tables
-- Select
SELECT cities.id, cities.name FROM cities, states WHERE state_id = states.id ORDER BY cities.id ASC;
