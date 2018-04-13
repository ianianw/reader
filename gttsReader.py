from gtts import gTTS
import os

tts = gTTS(text='一棵树', lang='zh-tw')
tts.save("good.mp3")
tts = gTTS(text='两棵树', lang='zh-tw')
os.system("mpg123 good.mp3")
tts.save("good.mp3")
os.system("mpg123 good.mp3")
