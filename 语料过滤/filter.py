import re
def qiubai_filter():
    mgc = load_mgc()
    with open("穿越过滤.txt", "a+",encoding= "UTF-8") as wri:
        with open("data/穿越.txt", "r", encoding="UTF-8") as f:
            flag = False
            for line in f:
                if line.startswith("帖子："):
                    joke = line.split("帖子：")[1]
                    flag = False
                    for word in mgc:
                        if joke.find(word) != -1:
                            flag = True
                            print(word)
                            print(joke)
                            break
                    if flag:
                        continue
                    wri.write(joke)


def douban_filter():
    with open("豆瓣电影.txt", "w", encoding= "UTF-8") as wri:
        with open("data/豆瓣2.txt", "r", encoding="UTF-8") as f:
            flag = False
            comment = ""
            for line in f:
                if line.strip() == "":
                    continue
                if line.startswith("问题："):
                    if flag is True:
                        comment = re.sub(u'\[\w*\]', '', comment)
                        wri.write(comment+"\n\n")
                        comment = ""
                        flag = False
                    film = line.split("问题：")[1]
                    film = re.sub(u'\[\w*\]', '', film)
                    if film.strip() != "" and re.search(u'[\uAC00-\uD7A3]', film) is None and re.search(u'[\u0800-\u4e00]', film) is None \
                            and len(line) <= 54:
                        wri.write(film)
                        flag = True
                        continue
                if flag is True:
                    if line.startswith("回复："):
                        comment = line.split("回复：")[1].strip()
                    else:
                        comment += line.strip()


def load_mgc():
    mgc = set()
    with open("data\敏感词\百度敏感词（需去重）.txt", "r", encoding="GBK") as f:
        for line in f:
            if line.strip() == "":
                continue
            mgc.add(line.strip())
    list163 = ["网易","网易云","云音乐","丁磊","丁三石","评论","收藏","下载","付费","我作为一个"]
    for word in list163:
        if word.strip() == "":
            continue
        mgc.add(word)
    return mgc


def douban_filter_2():
    mgc = load_mgc()
    my_list = []
    with open("豆瓣电影2.txt", "w", encoding= "UTF-8") as wri:
        with open("豆瓣电影.txt", "r", encoding="UTF-8") as f:
            a = f.readlines()
            for i in range(int(len(a)/3)):
                if len(a[i*3]) < 50 and len(a[i*3+1]) < 50:
                #if True:
                    flag = False
                    for word in mgc:
                        if a[i*3].find(word) != -1 or a[i*3+1].find(word) != -1 \
                                or a[i*3].strip() == "" or a[i*3+1].strip() == "":
                            flag = True
                            print(word)
                            print(a[i*3])
                            print(a[i*3+1])
                            break
                    if flag:
                        continue
                    if (a[i*3], a[i*3+1]) not in my_list:
                        wri.write(a[i*3])
                        wri.write(a[i*3+1]+"\n")
                        my_list.append((a[i*3], a[i*3+1]))


if __name__ == "__main__":
    douban_filter()
    douban_filter_2()


