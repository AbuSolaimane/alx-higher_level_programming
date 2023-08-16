-- Lists all shows contained.
SELECT tv.title, tvg.genre_id
	FROM tv_shows tv LEFT JOIN tv_show_genres tvg
	ON tv.id = tvg.show_id
	ORDER BY tv.title ASC, tvg.genre_id ASC;
