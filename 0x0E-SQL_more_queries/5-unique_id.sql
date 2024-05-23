-- a script that creates the table on my MySQL server

CREATE TABLE IF NOT EXISTS unique_id
	(id INT DEFAULT 1,
	UNIQUE (ID),
	name VARCHAR(256));
