-- A script that lists all comedy shows

SELECT tv_shows.title
FROM tv_shows_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
