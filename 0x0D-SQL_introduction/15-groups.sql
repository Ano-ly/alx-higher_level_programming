-- displays records with identical scores and their count value
SELECT score AS "score",
	COUNT(score) AS "number"
FROM second_table
GROUP BY score
ORDER BY number DESC;
