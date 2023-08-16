-- Lists all shows contained
SELECT tv.title, tvg.genre_id
	FROM tv_shows tv LEFT JOIN tv_show_genres tvg
	on tv.id = tvg.show_id
	WHERE tvg.genre_id IS NULL
	ORDER BY tv.title ASC, tvg.genre_id ASC;
