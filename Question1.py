# 1. Below is a database diagram 1. Below is a database diagram
# Write a query that will display the results below (Note: some columns might be renamed
# but use the column names above). It should only show 2020 data and order by driver
# points



SELECT 
    r.race_year,
    r.race_name,
    r.race_date,
    c.circuit_location,
    d.driver_name,
    d.driver_number,
    d.driver_nationality,
    con.name AS team,
    res.grid,
    res.fastest_lap,
    res.points
FROM 
    races r
JOIN 
    circuits c ON r.circuit_id = c.circuit_id
JOIN 
    results res ON r.race_id = res.race_id
JOIN 
    drivers d ON res.driver_id = d.driver_id
JOIN 
    constructors con ON res.constructor_id = con.constructor_id
WHERE 
    r.race_year = 2020
ORDER BY 
    res.points DESC;
