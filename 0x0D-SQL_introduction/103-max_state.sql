-- States and their maximum temperature
-- Select statement
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state;
