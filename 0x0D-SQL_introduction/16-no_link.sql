-- Lists all records based on certain conditions
-- Record must have a name, display score and name,
-- display in descending order by score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
