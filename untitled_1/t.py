import re
a = "第一眼看到歌名，有没有人瞬间想起你曾经喜欢的某个girl [啊]"
b = re.sub(u'\[\w*\]', '', a)
print(a)