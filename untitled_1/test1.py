def string_switch(x, y, z):
    with open(x, "r", encoding="utf-8") as f:
        # readlines以列表的形式将文件读出
        lines = f.readlines()

    with open(x, "w", encoding="utf-8") as f_w:
        # 定义一个数字，用来记录在读取文件时在列表中的位置
        n = 0
        # 默认选项，只替换第一次匹配到的行中的字符串
        flag = 0
        for line in lines:
            if y in line:
                index = lines.index(line)
                if index % 2 == 0:
                    line = line.replace(y, "你")
                else:
                    line = line.replace(y, "我")
            f_w.write(line)


string_switch("小冰.txt", "小冰", " ")