--  lists all cities contained in the database
SELECT c.id, c.name, s.name FROM cities c NATURAL JOIN
	states s ORDER BY c.id ASC;
