-- lists all genres
SELECT name, SUM(tsr.rate) 'rating' FROM tv_genres tg
	INNER JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
	INNER JOIN tv_show_ratings tsr ON tsg.show_id = tsr.show_id
	GROUP BY name
	ORDER BY rating DESC;
