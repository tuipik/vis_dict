# coding: utf8

import requests
import json

rs = requests.get('http://www.7english.ru/dictionary.php?id=2000&letter=all')

from bs4 import BeautifulSoup
root = BeautifulSoup(rs.content, 'html.parser')

en_ru_items = {}

for tr in root.select('tr'):
    # У строк в таблице перевода есть аттрибут onmouseover
    if 'onmouseover' not in tr.attrs:
        continue

    td_list = [td.text.strip() for td in tr.select('td')]

    # Количество ячеек в таблице со словами -- 9
    if len(td_list) != 9 or not td_list[1] or not td_list[5]:
        continue

    en = [td_list[1]]
    transcription = [td_list[3]]
    ru = [td_list[5]]

    print(td_list)
    en_ru_items.update(dict(zip(en, [transcription, ru])))
    print(len(en_ru_items), en_ru_items)

    with open('en_ru_dict.json', 'w', encoding='utf-8') as fp:
        json.dump(en_ru_items, fp, ensure_ascii=False)
