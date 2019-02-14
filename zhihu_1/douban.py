import requests
from bs4 import BeautifulSoup
import time
import re
for p in range(0, 9):
    time.sleep(0.5)
    url = "https://movie.douban.com/top250?start=" + str(p*25) + "&filter="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    cookies = {
        'cookie':'bid=LoW-gcbNw4s; gr_user_id=89963d41-6d51-4aa6-80a5-2ea3b589188e; _vwo_uuid_v2=D79228CDBBAEE6BC0D96FF7E6E4BFD918|03ccdfcc181f1981879f36ec34eed339; __utmz=30149280.1528873027.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap=1; ps=y; ll="108288"; viewed="5414391_26986954_26958126_3360807_1103015"; __yadk_uid=96fRnsrWV5DjWpq8rcL8J4Qn6mtVS6ho; ct=y; __utma=30149280.1103338133.1528706829.1529902147.1529915753.17; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1529915789%2C%22https%3A%2F%2Fwww.douban.com%2Fgroup%2Fblabla%2F%3Fref%3Dsidebar%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.154466763.1528883281.1528942649.1529915789.3; __utmb=223695111.0.10.1529915789; __utmz=223695111.1529915789.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/group/blabla/; loc-last-index-location-id="108288"; __utmc=30149280; __utmc=223695111; __utmb=30149280.69.5.1529915988220; ue="544286175@qq.com"; dbcl2="49393504:Kij6rNHequU"; ck=Mhm3; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=3513548a83660639.1528883281.3.1529922075.1528942861.'
    }
    page = requests.get(url,cookies=cookies,headers=headers)
    soup = BeautifulSoup(page.text,"lxml")
    allp = soup.findAll(class_ = 'info')
    for each in allp:
        time.sleep(0.5)
        answer = each.find('a')
        url = answer["href"]
        page = requests.get(url,cookies=cookies,headers=headers)
        soup = BeautifulSoup(page.text, "lxml")
        h1 = soup.find("h1")
        title = h1.text
        print(title)
        pattern = re.compile(r"\n", re.S)
        title = pattern.sub('', title)
        comment = soup.find_all(class_ = "comment")
        for c in comment:
            with open("豆瓣.txt", "a+", encoding="utf-8") as f:
                f.write("问题："+title+'\n')
                f.write('回复：' + c.find("p").text+'\n')
                f.close()