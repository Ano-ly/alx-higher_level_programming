-- Select from two tables
-- Select
SELECT cities.id, cities.name FROM cities, states WHERE states.name =
'Carlifornia' ORDER BY cities.id ASC;
