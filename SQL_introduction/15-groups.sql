-- Lists the number of records with the same score in second_table
-- Displays score and number of records for each score
-- Results are sorted by the number of records (descending)
SELECT score, COUNT(*) as number
FROM second_table 
GROUP BY score
ORDER BY score DESC;
