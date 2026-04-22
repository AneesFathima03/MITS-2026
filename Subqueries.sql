 -- Clients registered by staff earning > 20000
SELECT c.clientNo, c.fName, c.lName
FROM Client c
WHERE c.clientNo IN (
  SELECT r.clientNo
  FROM Registration r
  WHERE r.staffNo IN (
    SELECT s.staffNo FROM Staff s WHERE s.salary > 20000
  )
);