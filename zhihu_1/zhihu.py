import urllib.request
from bs4 import BeautifulSoup
import re
for p in range(1,14):
    url = "https://www.zhihu.com/collection/106496199?page=" + str(p)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page,"lxml")
    allp = soup.findAll(class_ = 'zm-item')
    for each in allp:
        answer = each.findNext(class_ = 'content')
        problem = each.findNext(class_ = 'zm-item-title')
        if len(answer.text) > 100:
            continue
        print(problem.text)
        print(answer.next)
        ans = str(answer.next)
        pattern = re.compile(r'<[^>]+>', re.S)
        ans = pattern.sub('', ans)
        with open("知乎2.txt", "a+", encoding="utf-8") as f:
            f.write('问题：' + problem.text+'\n')
            f.write('回复：' + ans+'\n')
            f.close()