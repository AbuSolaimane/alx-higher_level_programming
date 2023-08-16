-- uses 
SELECT name FROM tv_genres
	WHERE name NOT IN (SELECT name FROM tv_genres tg
		LEFT JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
		LEFT JOIN tv_shows ts ON tsg.show_id = ts.id
		WHERE tv_shows.title = 'Dexter')
	GROUP BY name
	ORDER BY name ASC;
