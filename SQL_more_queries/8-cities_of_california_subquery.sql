-- Lists all cities of California found in the hbtn_0d_usa database
-- Uses a subquery to find California's id without using JOIN
SELECT cities.id, cities.name FROM cities
WHERE state_id = (
    SELECT states.id FROM states 
    WHERE name = 'California'
)
ORDER BY cities.id ASC;
