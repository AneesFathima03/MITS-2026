-- Properties per city (only if > 1 listing)
SELECT city, COUNT(*) AS property_count
FROM PropertyForRent
GROUP BY city
HAVING COUNT(*) > 1
ORDER BY property_count DESC;