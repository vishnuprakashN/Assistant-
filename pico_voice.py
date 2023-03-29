from gtts import gTTS
  
import os
  
mytext = 'my name is vishnu prakash N'
  
language = 'en-IN'
  
myobj = gTTS(text=mytext, lang=language, slow=False)  
myobj.save("welcome.mp3")  
os.system("mpg321 welcome.mp3")
