-- Lists all records with score >= 10 from second_table
-- Records are ordered by score (highest first)
SELECT score, name
FROM second_table
WHERE score >=10
ORDER BY score DESC;
