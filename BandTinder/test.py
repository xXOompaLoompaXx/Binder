# Assuming insruments is a list of instrument names and genre is defined
instruments = ["Drums", "El-Guitar", "Vocals", "Bass"]  # example list
genre = "Rock"  # example genre

sql = """
SELECT DISTINCT *
FROM 
"""
parts = []
for ins in instruments:
    parts.append (f"""
    (SELECT PG.pk
    FROM Prefers_Genre PG, Plays P
    WHERE PG.pk=P.pk and PG.genre='{genre}' and P.instrument='{ins}')
    """)
    
sql += ",".join(parts)

print(sql)

