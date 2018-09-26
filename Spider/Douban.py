import requests
import re
import json

def open_page(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    response =requests.get(url, headers=kv)
    if response.status_code == 200:
        return response.text
    return None

def parse_page(html):
    patten = re.compile('<li>.*?title">(.*?)</span>.*?class="">(.*?)<br>.*?average">(.*?)</span>.*?</li>', re.S)
    items = re.findall(patten, html)
    for item in items:
        yield {
            'name': item[0],
            'person': item[1],
            'score': item[2]
        }

def write(content):
    with open('douban.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()

def main(start):
    url = 'https://movie.douban.com/top250?start='+str(start)
    html = open_page(url)
    for item in parse_page(html):
        print(item)
        write(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*25)