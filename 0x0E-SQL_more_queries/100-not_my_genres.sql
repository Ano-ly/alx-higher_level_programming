-- List of genres not linked to Dexter
-- Select statement
SELECT DISTINCT name FROM ((tv_shows LEFT JOIN tv_show_genres ON tv_shows.id=show_id) RIGHT JOIN tv_genres ON genre_id=tv_genres.id) WHERE genre_id NOT IN (SELECT genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id=show_id WHERE show_id=8) ORDER BY name ASC;
