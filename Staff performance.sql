SELECT s.staffNo, s.fName, s.lName, COUNT(r.clientNo) AS client_count
FROM Staff s
LEFT JOIN Registration r ON s.staffNo = r.staffNo
GROUP BY s.staffNo, s.fName, s.lName
ORDER BY client_count DESC, s.staffNo;