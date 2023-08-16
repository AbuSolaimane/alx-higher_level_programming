-- lists all shows
SELECT title, name FROM tv_shows ts
	LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
	LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id
	ORDER BY title ASC, name ASC;
