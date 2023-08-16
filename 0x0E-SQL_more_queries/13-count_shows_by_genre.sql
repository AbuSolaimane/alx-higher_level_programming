-- Lists all genres
SELECT tv.name AS `genre`,
	COUNT(*) AS `number_of_shows`
	FROM `tv_genres` AS tv INNER JOIN `tv_show_genres` AS tvg
	ON tv.id = tvg.genre_id
	GROUP BY tv.name
	ORDER BY `number_of_show` DESC;
