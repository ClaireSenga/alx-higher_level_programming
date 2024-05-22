-- a script that creates a table and adds mul rows
-- table: second_table
-- database: hbtn_0c_0

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

-- scripts should create 4 records

INSERT INFO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INFO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INFO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INFO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
