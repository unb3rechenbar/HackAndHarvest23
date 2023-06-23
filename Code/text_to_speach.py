import pyttsx3

# Initialisiere den Text-to-Speech-Engine
engine = pyttsx3.init()

# Ändere die Stimme zur "Microsoft Hedda"-Stimme
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #einzige deutsche Stimme

# Konvertiere Text in Sprache
engine.say("Hallo, mein Name ist Heymex. Darf ich ihre Sauerstoffsättigung messen?")

# Warte, bis die Konvertierung abgeschlossen ist
engine.runAndWait()

# Gib die verfügbaren Stimmen aus
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Stimme: {voice.name}")
    print(f" - ID: {voice.id}")
    print(f" - Geschlecht: {voice.gender}")
    print(f" - Alter: {voice.age}")