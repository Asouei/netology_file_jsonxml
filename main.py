# модуль для Json

import json
import xml.etree.ElementTree as ET
from pprint import pprint


def get_words(all_news):

    all_list = []
    final_list = []
    unique_list = []

    all_list = all_news.split(" ")
    all_list.sort(key=len, reverse=True)

    for strings in all_list:
        if len(strings) >= 6:
            final_list.append(strings)
        else:
            continue

    unique_list = list(set(final_list))

    counts = []

    for unique in unique_list:
        count = 0
        for word in final_list:
            if unique == word:
                count += 1
            else:
                continue

        counts.append((count, unique))

    counts.sort(reverse=True)
    n = 0

    for elements in counts:
        if n != 10:
            print(f'Слово "{elements[1]}" - повторяется {elements[0]} раз.')
            n += 1
        else:
            break
    print('---------------------')
    print()

def main_json():

    all_news = ''


    print()
    print('Для Json файла')
    print()

    with open('newsafr.json', newline='', encoding="utf-8") as f:
        json_data = json.load(f)
        # pprint(json_data['rss']['channel']['items'])

        items = json_data['rss']['channel']['items']
        for news in items:
            all_news += news['description']

    get_words(all_news)

def main_xml():

    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()

    all_news = ''

    print()
    print('Для XML файла')
    print()

    news_list = root.findall('channel/item')

    for news in news_list:
        description = news.find('description').text
        all_news += description

    get_words(all_news)


main_json()
main_xml()