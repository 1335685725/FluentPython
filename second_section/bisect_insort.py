import random
import bisect

SIZE = 7

random.seed(111)

my_list = []

for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print(f"{new_item:2} ->", my_list)