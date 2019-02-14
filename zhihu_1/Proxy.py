import requests
from bs4 import BeautifulSoup
import time


def getProxy():
    for page in range(1, 5):
        IPurl = 'http://www.xicidaili.com/nn/%s' %page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        }
        time.sleep(2)
        rIP=requests.get(IPurl,headers=headers)
        IPContent=rIP.text
        soupIP = BeautifulSoup(IPContent,"lxml")
        trs = soupIP.find_all('tr')
        ProxiesList = []
        for tr in trs[1:]:
            tds = tr.find_all('td')
            ip = tds[1].text.strip()
            port = tds[2].text.strip()
            protocol = tds[5].text.strip()
            if protocol == 'HTTP':
                httpResult = 'http://' + ip + ':' + port
                proxies = {
                    "http": httpResult
                }
            elif protocol =='HTTPS':
                httpsResult = 'https://' + ip + ':' + port
                proxies = {
                    "https": httpsResult
                }
            try:
                requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
                ProxiesList.append(proxies)
                with open("ip.txt", "a+", encoding="utf-8") as f:
                    f.write(str(proxies) + '\n')
                    f.close()
            except Exception as e:
                print(e)
    return ProxiesList


if __name__ == '__main__':
    getProxy()