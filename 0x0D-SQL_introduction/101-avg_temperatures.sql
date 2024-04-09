-- Cities and their average temperature, descending order
-- Select statement
SELECT city, AVG(value) AS  avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
