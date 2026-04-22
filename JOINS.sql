-- Properties with owner names
SELECT p.propertyNo, p.street, p.city, o.fName AS ownerFirst, o.lName AS ownerLast
FROM PropertyForRent p
JOIN PrivateOwner o ON p.ownerNo = o.ownerNo;