-- Cities by States
-- select join
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN satates ON states.id = cities.state_id ORDER BY cities.id; 
