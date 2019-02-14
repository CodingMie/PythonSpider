import re
import os

def douban_filter():
    with open("小冰过滤.txt", "w", encoding= "UTF-8") as wri:
        with open("data/小冰微博评论.txt", "r", encoding="UTF-8") as f:
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
    list163 = ["","微博","博主","新浪","借个楼","关注","取关","评论","推主","传送门","投稿","po主","层主","湉湉","肖骁",
               "恬恬","奇葩说","电视节目","薇姐","马东","@","网页链接","图片评论","博主","李总", "不二","大叔"]
    for word in list163:
        if word.strip() == "":
            continue
        mgc.add(word)
    return mgc


def filter():
    mgc = load_mgc()
    root = "data\微博"
    for dirpath, dirnames, filenames in os.walk(root):
        for filepath in filenames:
            filename = os.path.join(dirpath, filepath)
            with open(filename, "r", encoding= "UTF-8") as f:
                with open(filepath+"_0803.txt", "w", encoding="UTF-8") as wri:
                    a = f.readlines()
                    for i in range(int(len(a)/2)):
                        q = a[i*2]
                        ans = a[i*2+1]
                        if len(q.split("问题：")) == 2 and len(ans.split("回复：")) == 2:
                            q = q.split("问题：")[1].strip()
                            ans = ans.split("回复：")[1].strip()
                            q = re.sub(u'\[\w*\]', '', q)
                            ans = re.sub(u'\[\w*\]', '', ans)
                            q = re.sub('[/:#]','',q)
                            ans = re.sub('[/:#]', '', ans)
                            if q.strip() == "" or ans.strip() == "" or re.search(u'[\uAC00-\uD7A3]', q) is not None \
                                    and re.search(u'[\u0800-\u4e00]', q) is not None:
                                continue
                            flag = False
                            for word in mgc:
                                if q.find(word) != -1 or ans.find(word) != -1 \
                                        or q.strip() == "" or ans.strip() == "":
                                    flag = True
                                    print(word)
                                    print(q)
                                    print(ans)
                                    break
                            if flag is True:
                                continue
                            wri.write(q.strip()+"\n")
                            wri.write(ans.strip()+"\n\n")


def filter_2():
    root = "data\小冰过滤26.5万.txt"
    for dirpath, dirnames, filenames in os.walk(root):
        for filepath in filenames:
            filename = os.path.join(dirpath, filepath)
            with open(filename, "r", encoding= "UTF-8") as f:
                with open(filepath+"0815.txt", "w", encoding="UTF-8") as wri:
                    a = f.readlines()
                    for i in range(int(len(a) / 3)):
                        q = a[i * 3]
                        ans = a[i * 3 + 1]
                        if 0 < len(q.strip()) <= 15 and 0 < len(ans.strip()) <= 15:
                            wri.write(q)
                            wri.write(ans+"\n")


if __name__ == "__main__":
    filename = "data\小冰过滤26.5万.txt"
    with open(filename, "r", encoding="UTF-8") as f:
        with open("小冰过滤0815.txt", "w", encoding="UTF-8") as wri:
            a = f.readlines()
            for i in range(int(len(a) / 3)):
                q = a[i * 3]
                ans = a[i * 3 + 1]
                if 0 < len(q.strip()) <= 15 and 0 < len(ans.strip()) <= 15:
                    wri.write(q)
                    wri.write(ans + "\n")


