SELECT b.branchNo, b.street, b.city, COUNT(s.staffNo) AS staff_count
FROM Branch b
LEFT JOIN Staff s ON b.branchNo = s.branchNo
GROUP BY b.branchNo, b.street, b.city
ORDER BY b.branchNo;