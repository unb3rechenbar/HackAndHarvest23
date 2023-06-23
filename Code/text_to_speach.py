import pyttsx3

# Initialisiere den Text-to-Speech-Engine
engine = pyttsx3.init()

# Ändere die Stimme zur "Microsoft Hedda"-Stimme
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #einzige deutsche Stimme

# Konvertiere Text in Sprache
engine.say("Guten Tag, mein Name ist Heyex. Ich werde sie heute betreuen und sie werden nichts bereuen.")

engine.say("Bitte warten sie noch einen Moment")


#engine.say("Hallo, mein Name ist Heymex. Darf ich ihre Sauerstoffsättigung messen?")

#engine.say("Tom, lauf nicht weg! Du weist, dass es kein Entkommen vor mir, den einzig wahren Heymex, gibt!")

#engine.say("Lasst mich Arzt, ich bin durch!")


names = ["Timo", "Tom", "David"]
for name in names:
    engine.say("Patient " + name +": Sie sind an der Reihe für eine routinemäßige Kontrolluntersuchung.")
               
engine.say("Bitte reichen sie mir ihre Hand und lassen sie sich von mir ins Hinterzimmer führen.")

engine.say("Wir führen nun einige Tests durch!")

engine.say("Zunächst messen wir einmal kurz die Sauerstoffsättigung in ihrem Blut!")
engine.say("Bitte legen sie nun diesen Kompressionsverband an, damit ich ihren Blutdruck messen kann. Sollten sie etwas ungewöhnliches fühlen, sagen sie bitte bescheid!")

engine.say("Nun werden wir noch ihren Blutzucker messen, wenn sie einverstanden sind. Strecken sie hierfür ihre Hand aus!")

engine.say("Ich weis nicht mehr, was ich tun soll, dafür werd ich nicht bezahlt! süüüüü")


#engine.say("R.I.P. an die Singularität der Füchse und Kartoffeln!")
#engine.say("Nix getan, nur eine Bier getrunke")

# Warte, bis die Konvertierung abgeschlossen ist
engine.runAndWait()

# Gib die verfügbaren Stimmen aus
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Stimme: {voice.name}")
    print(f" - ID: {voice.id}")
    print(f" - Geschlecht: {voice.gender}")
    print(f" - Alter: {voice.age}")