-- Displays contents of second_table ordered by score
-- where score >= 10
SELECT score, name FROM second_table
WHERE score > 9
ORDER BY score DESC, name;
