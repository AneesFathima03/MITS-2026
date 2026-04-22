-- Names that appear in Staff or PrivateOwner (deduped)
SELECT fName, lName FROM Staff
UNION
SELECT fName, lName FROM PrivateOwner;