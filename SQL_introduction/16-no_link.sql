-- Lists all records of second_table excluding rows without a name value
-- Results are ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
