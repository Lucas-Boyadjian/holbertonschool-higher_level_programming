-- Lists all cities with their corresponding state names
-- Uses JOIN to connect cities and states tables on the state_id foreign key
SELECT cities.id, cities.name, states.name 
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
