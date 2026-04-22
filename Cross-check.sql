SELECT 
    p.propertyNo,
    p.street AS property_street,
    p.city AS property_city,
    s.fName || ' ' || s.lName AS staff_name,
    b.city AS branch_name
FROM PropertyForRent p
JOIN Staff s ON p.staffNo = s.staffNo
JOIN Branch b ON p.branchNo = b.branchNo
ORDER BY p.propertyNo;