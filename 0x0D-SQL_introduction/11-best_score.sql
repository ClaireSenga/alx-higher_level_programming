-- a script that list all records with condition
-- with score >= 0 in second_table of db

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
