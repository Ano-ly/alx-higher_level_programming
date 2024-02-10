-- lists records in second_table where name is not NULL
SELECT score, name FROM second_table
	WHERE name != "NULL"
	ORDER BY score DESC;
