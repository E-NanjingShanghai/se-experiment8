import requests
import re

url = 'https://movie.douban.com/top250'
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'

}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
# print(response.text)
h = response.text
pattern = re.compile(r'<img width="100" alt="(?P<name>.*?)"'
                     r'.*?<p class="">.*? '
                     r'导演: (?P<director>.*?)&nbsp.*?'
                     r'主演: (?P<actors>.*?)<br>'
                     r'(?P<year>.*?)&nbsp;.*?'
                     r'/&nbsp;(?P<country>.*?)&nbsp;.*?'
                     r';(?P<type>.*?)</p>.*?'
                     r'<span class="rating_num" property="v:average">(?P<mark>.*?)</span>.*?'
                     r'<span>(?P<evaluate>.*?)</span>', re.S)
result = pattern.finditer(h)
for item in result:
    with open('豆瓣电影信息.txt', 'a', encoding='utf-8') as fp:
        fp.write('\n')
        fp.write(item.group('name'))
        fp.write('\n')
        fp.write(item.group('director'))
        fp.write('\n')
        fp.write(item.group('actors'))
        fp.write('\n')
        fp.write(item.group('year').strip())
        fp.write('\n')
        fp.write(item.group('country'))
        fp.write('\n')
        fp.write(item.group('type'))
        fp.write('\n')
        fp.write(item.group('mark'))
        fp.write('\n')
        fp.write(item.group('evaluate'))
        fp.write('\n')

print('爬取完成')

