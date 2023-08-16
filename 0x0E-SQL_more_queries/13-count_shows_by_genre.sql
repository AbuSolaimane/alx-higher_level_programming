-- Lists all genres
SELECT tv.name AS genre,
	COUNT(tvg.genre_id) AS number_of_shows
	FROM tv_genres tv INNER JOIN tv_show_genres tvg
	ON tv.id = tvg.genre_id
	GROUP BY genre
	ORDER BY number_of_show DESC;
