-- lists all Comedy
SELECT title FROM tv_shows tv
	LEFT JOIN tv_show_genres tvg ON tv.id = tvg.show_id
	LEFT JOIN tv_genres tg ON tvg.genre_id = tg.id
	WHERE tg.name = 'Comedy'
	GROUP BY title
	ORDER BY title ASC;
