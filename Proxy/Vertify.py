import urllib.request
url = "https://weibo.com/messages?leftnav=1&wvr=6"  #打算抓取内容的网页
proxy_ip={'http': '121.231.168.206:6666'}  #想验证的代理IP
proxy_support = urllib.request.ProxyHandler(proxy_ip)
opener = urllib.request.build_opener(proxy_support)
opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64)")]
urllib.request.install_opener(opener)
print(urllib.request.urlopen(url).read())