--  lists all cities contained in the database
SELECT c.id, c.name, s.name FROM cities c 
		      INNER JOIN states s
		     	      ON s.id = c.state_id
			ORDER BY c.id ASC;
