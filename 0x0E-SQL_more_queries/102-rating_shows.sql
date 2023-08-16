-- lists all shows
SELECT title, SUM(tsr.rate) 'rating' FROM tv_shows ts
	LEFT JOIN tv_show_ratings tsr ON tsr.show_id = ts.id
	GROUP BY title
	ORDER BY rating DESC;
