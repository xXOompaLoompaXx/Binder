--See if a band exists that has players 1, 2 ,3
SELECT band_id
FROM band_contains
WHERE pk IN (1, 2, 3)
GROUP BY band_id
HAVING COUNT(DISTINCT pk) = 3;

-- 
SELECT DISTINCT *
FROM 
(SELECT PG.pk
FROM Prefers_Genre PG, Plays P
WHERE PG.pk=P.pk and PG.genre='Rock' and P.instrument='Drums'), 
(SELECT PG.pk
FROM Prefers_Genre PG, Plays P
WHERE PG.pk=P.pk and PG.genre='Rock' and P.instrument='El-Guitar'),
(SELECT PG.pk
FROM Prefers_Genre PG, Plays P
WHERE PG.pk=P.pk and PG.genre='Rock' and P.instrument='Vocals'),
(SELECT PG.pk
FROM Prefers_Genre PG, Plays P
WHERE PG.pk=P.pk and PG.genre='Rock' and P.instrument='Bass')