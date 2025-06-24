-- Script that lists all shows and all genres linked to each show from the database
-- If a show doesn't have a genre, NULL should be displayed in the genre column
-- Results are sorted in ascending order by show title and genre name
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_shows.id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id 
ORDER BY tv_shows.title, tv_genres.name ASC;
