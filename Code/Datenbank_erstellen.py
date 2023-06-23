
"""
# Eine Tabelle erstellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Patienten
                  (Aktiv, Name, Zimmernummer, Bett, Alter, Aufenthaltsgrund, Puls, Sauerstoffsaettigung, last_updated)''') #in den gängigen Einheiten

# Datensätze in die Tabelle einfügen
cursor.execute("INSERT INTO Patienten VALUES (True, 'Max Mustermann', 101, 2, 44, 'gebrochenes Bein', 70, 0.97, '23.06.23 15:38')")
cursor.execute("INSERT INTO Patienten VALUES (True, 'Erika Musterfrau', 101, 1, 80, 'Kammerflimmern', 100,0.90, '23.06.23 19:23')")
cursor.execute("INSERT INTO Patienten VALUES (False, 'Anton Ziegler', 101, 3, 46, 'Grippe', 90,0.95, '22.06.23 23:33')")
cursor.execute("INSERT INTO Patienten VALUES (True, 'Matze Fuchs', 404, 1, 10, 'Borreliose', 75,0.96, '23.6.23 13:34')")
cursor.execute("INSERT INTO Patienten VALUES (True, 'Salma Nura', 301, 1, 43, 'Husten', 90, 0.90, '23.6.23 15:43')")
cursor.execute("INSERT INTO Patienten VALUES (False, 'Dixie Normus',202, 1, 34, 'Lungenembolie',70,0.89,70, '23.06.23 21:08')")
"""



import sqlite3

# Verbindung zur Datenbank erstellen (falls nicht vorhanden wird sie neu erstellt)
conn = sqlite3.connect('Krankenhaus.db')

# Ein Cursor-Objekt erstellen
cursor = conn.cursor()

# Eine Tabelle erstellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Patienten
                  (Aktiv, Name, Zimmernummer, Bett, Alterr, Aufenthaltsgrund, Puls, Sauerstoffsaettigung, last_updated)''') #in den gängigen Einheiten


# Datensätze in die Tabelle einfügen
cursor.execute("INSERT INTO Patienten VALUES (True, 'Max Mustermann', 101, 2, 44, 'gebrochenes Bein', 70, 0.97, '23.06.23 15:38')")
cursor.execute("INSERT INTO Patienten VALUES (True, 'Erika Musterfrau', 101, 1, 80, 'Kammerflimmern', 100,0.90, '23.06.23 19:23')")
cursor.execute("INSERT INTO Patienten VALUES (False, 'Anton Ziegler', 101, 3, 46, 'Grippe', 90,0.95, '22.06.23 23:33')")
cursor.execute("INSERT INTO Patienten VALUES (True, 'Matze Fuchs', 404, 1, 10, 'Borreliose', 75,0.96, '23.6.23 13:34')")
cursor.execute("INSERT INTO Patienten VALUES (True, 'Salma Nura', 301, 1, 43, 'Husten', 90, 0.90, '23.6.23 15:43')")
cursor.execute("INSERT INTO Patienten VALUES (False, 'Dixie Normus',202, 1, 34, 'Lungenembolie',70,0.89, '23.06.23 21:08')")

# Änderungen speichern
conn.commit()

# Datensätze auslesen und ausgeben
cursor.execute("SELECT * FROM Patienten")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Verbindung schließen
conn.close()
