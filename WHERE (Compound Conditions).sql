-- Properties in Glasgow with rent < 500
SELECT propertyNo, street, city, rent
FROM PropertyForRent
WHERE city = 'Glasgow' AND rent < 500;