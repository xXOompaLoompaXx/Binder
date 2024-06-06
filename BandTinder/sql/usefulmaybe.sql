SELECT band_id
FROM band_contains
WHERE pk IN (1, 2, 3)
GROUP BY band_id
HAVING COUNT(DISTINCT pk) = 3;


