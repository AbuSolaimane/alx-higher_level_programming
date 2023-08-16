-- lists all genres 
SELECT tv.name FROM tv_genres tv
	INNER JOIN tv_show_genres tvg
	ON tv.id = tvg.genre_id
	INNER JOIN tv_shows tv2
	ON tvg.show_id = tv2.id
	WHERE tv.title = "Dexter"
	ORDER BY tv.name;
