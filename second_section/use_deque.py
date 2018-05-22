from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
# 队列旋转操作，n>0时，将队列最右边的n个元素移动到最左边
# n<0时， 将队列最左边的n个元素移动到最右边
dq.rotate(4)
print(dq)
dq.rotate(-3)
print(dq)
# 对一个已满的队列尾部增加一个元素，头部的元素会被挤掉,对头部操作则尾被挤掉
dq.appendleft(-1)
print(dq)
dq.extend([11, 22 ,33])
print(dq)
dq.extendleft([22, 33, 44])
print(dq)