SELECT city, COUNT(name) AS public_schools FROM schools
WHERE type = "Public School"
GROUP BY city
ORDER BY public_schools DESC, city
LIMIT 10;
