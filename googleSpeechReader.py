import os
from random import shuffle

import time

import yaml
from google_speech import Speech

tw_lines = []
replace_lines = {}
separate_lines = {}

with open('words.txt', encoding='UTF8') as f:
    lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]
    backup_lines = list(lines)
    # shuffle(lines)

    index = 1
    for line in lines:
        timeout = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "timeout.yml")))
        if len(line) > 3:
            interval = timeout['Chn']['long interval']
            sleep = timeout['Chn']['long sleep']
            repeat_times = 3
        else:
            interval = timeout['Chn']['short interval']
            sleep = timeout['Chn']['short sleep']
            repeat_times = 2
        print("{0} - {1}".format(index, line))
        for x in range(0, repeat_times):
            if line in tw_lines:
                lang = "zh-TW"
                sox_effects = ("speed", "1.0")
                speech = Speech(replace_lines.get(line, line), lang)
                speech.play(sox_effects)
            elif line in separate_lines:
                lang = "zh-CN"
                sox_effects = ("speed", "1.0")
                separated_lines = separate_lines.get(line)
                for key in separated_lines.keys():
                    lang = separated_lines.get(key)
                    speech = Speech(replace_lines.get(key, key), lang)
                    speech.play(sox_effects)
            else:
                lang = "zh-CN"
                sox_effects = ("speed", "1.0")
                speech = Speech(replace_lines.get(line, line), lang)
                speech.play(sox_effects)
            time.sleep(sleep)

        index = index + 1
        backup_lines.remove(line)
        time.sleep(interval)

    print(backup_lines)
