# 创建一个从一个单词到其出现情况的映射

import re
import sys

word_re = re.compile(r"\w+")

index = {}
with open(sys.argv[1], encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start() +1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)
            # 等价于如下代码
            # if key not in index:
            #     index[key] = []
            # index[key].append(location)
# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])
