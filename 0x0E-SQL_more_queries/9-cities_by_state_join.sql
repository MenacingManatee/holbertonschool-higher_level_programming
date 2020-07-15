-- lists all the cities and states
-- in the database hbtn_0d_usa.
SELECT id, name, (SELECT name
FROM states
WHERE id=state_id) AS name
FROM cities
GROUP BY id, name
ORDER BY id;
