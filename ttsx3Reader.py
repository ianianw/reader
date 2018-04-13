from random import shuffle
import pyttsx3
import time

with open('/Users/iwu/Desktop/test', encoding='UTF8') as f:
    lines = f.readlines()

shuffle(lines)
engine = pyttsx3.init('nsss')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)
index = 1
for line in lines:
    print("{0} - {1}".format(index, line))
    index = index + 1
    engine.say(line)
    engine.runAndWait()
    # time.sleep(3)
    engine.say(line)
    engine.runAndWait()
    # time.sleep(15)
