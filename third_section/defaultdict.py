# 创建一个从一个单词到其出现情况的映射

import re
import sys
import collections

word_re = re.compile(r"\w+")

index = collections.defaultdict(list)
with open(sys.argv[1], encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start() +1
            location = (line_no, column_no)
            index[word].append(location)
            # 如果index中没有word记录，那么default_factory调用，这里产生一个空列表（list构造方法）赋值给index【word】
# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])