-- INSERT
INSERT INTO Client (clientNo, fName, lName, telNo, prefType, maxRent)
VALUES ('C100','Alice','Brown','07700123456','Flat',600);

-- UPDATE
UPDATE PropertyForRent
SET rent = 550
WHERE propertyNo = 'PG4';

-- DELETE
DELETE FROM Viewing
WHERE viewDate < '2023-01-01';