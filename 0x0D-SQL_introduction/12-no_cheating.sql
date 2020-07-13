-- Helps John cheat by dropping Bob's score to a tie
UPDATE `second_table`
SET `score`=10
WHERE `second_table`.`name`="Bob";
