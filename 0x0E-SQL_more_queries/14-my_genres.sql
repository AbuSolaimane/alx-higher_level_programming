-- select
SELECT name FROM tv_genres tv
	LEFT JOIN tv_show_genres tvg ON tv.id = tvg.genre_id
	LEFT JOIN tv_shows tv2 ON tvg.show_id = tv2.id
	WHERE tv2.title = 'Dexter'
	GROUP BY name
	ORDER BY name ASC;
