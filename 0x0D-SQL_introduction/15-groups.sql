-- lists the number of records with the same score in the table second_table
SELECT score, COUNT(*) AS number FROM second_table GROUB BY score ORDER BY COUNT(*) DESC;
