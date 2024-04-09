-- Display shows with no genre linked
-- Select statement
SELECT DISTINCT title, genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id WHERE genre_id is NULL ORDER BY title ASC, genre_id ASC;
