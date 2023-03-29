import pyttsx3

engine = pyttsx3.init()



voice_id = "hindi"

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")


newVoiceRate = 120
engine.setProperty('voice','english_rp+f3')
engine.setProperty('rate',newVoiceRate)
engine.say('hi how are you')
engine.runAndWait()
