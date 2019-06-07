from random import shuffle

import time

import requests
from google_speech import Speech
from requests import ConnectTimeout

with open('test', encoding='UTF8') as f:
    lines = f.readlines()
    # lines = list(set([line.replace('\n', '') for line in lines]))
    # backup_lines = list(lines)
    # shuffle(lines)
    dialogs = list()
    dialog = list()
    for line in lines:
        if line != '\n':
            dialog.append(line)
        else:
            dialogs.append(dialog)
            dialog = list()
    dialogs.append(dialog)

    # langs = ['en-au', 'en-au', 'en-au']
    langs = ['en-us', 'en-us']
    # langs = ['en-us']

    index = 1
    for dialog in dialogs:
        for lang in langs:
            for line in dialog:
                print("{0}".format(line))
                sox_effects = ("speed", "1.0")
                speech = Speech(line, lang)
                try:
                    speech.play(sox_effects)
                except (requests.exceptions.ConnectionError, ConnectTimeout) as e:
                    try:
                        speech.play(sox_effects)
                    except (requests.exceptions.ConnectionError, ConnectTimeout) as e:
                        # print(backup_lines)
                        exit()
                time.sleep(5)

            time.sleep(20)

        # backup_lines.remove(line)
        # time.sleep(8)
        # time.sleep(15)
