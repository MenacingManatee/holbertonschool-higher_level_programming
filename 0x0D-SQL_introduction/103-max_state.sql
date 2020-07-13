-- displays the top 3 max temperatures (Fahrenheit) by state ordered by
-- temperature (descending)
SELECT state, MAX(value) 'max_temp'
FROM temperatures
GROUP BY state
ORDER BY state, max_temp DESC
LIMIT 3;
