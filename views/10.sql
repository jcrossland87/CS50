SELECT english_title AS 'Lowest Entropy' FROM views
WHERE artist = "Hokusai"
ORDER BY entropy
LIMIT 1;
