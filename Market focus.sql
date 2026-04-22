SELECT city, COUNT(*) AS listing_count
FROM PropertyForRent
GROUP BY city
ORDER BY listing_count DESC, city;