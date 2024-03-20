-- Select from two tables
-- Select
SELECT cities.id, cities.name FROM cities, states WHERE states.name =
'California' ORDER BY cities.id ASC;
