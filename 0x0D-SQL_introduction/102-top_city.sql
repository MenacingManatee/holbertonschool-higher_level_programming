-- displays the average temperature (Fahrenheit) by city ordered by
-- temperature (descending)
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
WHERE month BETWEEN 7 and 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
