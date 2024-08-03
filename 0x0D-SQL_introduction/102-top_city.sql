-- Cities and their average temperature in July and August, max
-- Select statement
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 0,3;