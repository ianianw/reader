from random import shuffle

import time

import requests
from google_speech import Speech
from requests import ConnectTimeout

with open('test', encoding='UTF8') as f:
    lines = f.readlines()
    lines = list(set([line.replace('\n', '') for line in lines]))
    backup_lines = list(lines)
    shuffle(lines)

    # langs = ['en-au', 'en-au']
    # langs = ['en-us', 'en-us', 'en-us']
    langs = ["zh-CN"]

    index = 1
    for line in lines:
        print("{0} - {1}".format(index, line))
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
            # time.sleep(10)

        index = index + 1
        backup_lines.remove(line)
        time.sleep(3)
        # time.sleep(20)
