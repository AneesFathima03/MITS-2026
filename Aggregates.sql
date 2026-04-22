-- Average / Min / Max rent
SELECT ROUND(AVG(rent),2) AS avg_rent,
       MIN(rent) AS min_rent,
       MAX(rent) AS max_rent
FROM PropertyForRent;