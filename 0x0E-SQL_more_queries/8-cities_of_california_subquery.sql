-- lists all the cities of California that can be found
-- in the database hbtn_0d_usa.
SELECT state_id, name
FROM (
SELECT cities.state_id, cities.name
FROM cities
UNION ALL
SELECT states.id, states.name
FROM states
WHERE name="California"
) t
WHERE name!="California"
GROUP BY state_id, name
ORDER BY state_id;
