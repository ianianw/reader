from random import shuffle

import time
from google_speech import Speech

tw_lines = ['只得', '飘落']
replace_lines = {'种树': '众树',
                 '连长': '连涨',
                 '窗户': '窗粐',
                 '朝霞的朝。第八笔': '朝霞的招。第八笔',
                 '扇风点火': '山风点火',
                 '闷热的闷。第三笔': '闷热的。第三笔',
                 '翅膀的膀。第四笔': '翅膀的榜。第四笔',
                 '露珠的露。第十笔': '露珠的路。第十笔',
                 '仔细的仔。第三笔': '仔细的子。第三笔',
                 '结实的结。第三笔': '结实的接。第三笔',
                 '种瓜': '重瓜'}
separate_lines = {'找着': {'找': 'zh-CN', 'zháo': 'vi'}}

with open('test', encoding='UTF8') as f:
    lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]
    backup_lines = list(lines)
    shuffle(lines)

    index = 1
    for line in lines:
        print("{0} - {1}".format(index, line))
        for x in range(0, 2):
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
            time.sleep(3)

        index = index + 1
        backup_lines.remove(line)
        time.sleep(15)

    print(backup_lines)
