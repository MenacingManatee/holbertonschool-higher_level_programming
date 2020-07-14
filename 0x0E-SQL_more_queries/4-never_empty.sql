-- Creates a table id_not_null with columns id and name
-- ID is not required, but the default value is 1
CREATE TABLE IF NOT EXISTS id_not_null (
id INT DEFAULT 1,
name VARCHAR(256));
