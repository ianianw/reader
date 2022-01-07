import os
from random import shuffle

import time

import yaml
from google_speech import Speech
import requests
from requests import ConnectTimeout

with open('words.txt', encoding='UTF8') as f:
    lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]
    backup_lines = list(lines)
    # shuffle(lines)

    index = 1
    for line in lines:
        print("{0} - {1}".format(index, line))
        timeout = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "timeout.yml")))
        if len(line.split(' ')) > 2:
            langs = ['en-us', 'en-us', 'en-us']
            # langs = ['en-au', 'en-au']
            # langs = ['en-us']
            interval = timeout['Eng']['long interval']
            sleep = timeout['Eng']['long sleep']
        else:
            langs = ['en-us', 'en-us']
            interval = timeout['Eng']['long interval']
            sleep = timeout['Eng']['long sleep']
        for lang in langs:
            sox_effects = ("speed", "1.0")
            speech = Speech(line, lang)
            try:
                speech.play(sox_effects)
            except (requests.exceptions.ConnectionError, ConnectTimeout) as e:
                try:
                    speech.play(sox_effects)
                except (requests.exceptions.ConnectionError, ConnectTimeout) as e:
                    print(backup_lines)
                    exit()
            # time.sleep(2)
            time.sleep(interval)

        index = index + 1
        backup_lines.remove(line)
        # time.sleep(15)
        time.sleep(sleep)
