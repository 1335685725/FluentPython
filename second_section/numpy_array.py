import numpy

a = numpy.array(12)
print(a)
print(type(a))
print(a.shape)
# 改成三行四列
a.shape = (3, 4)
print(a)
print(a[2])
print(a[1, 2])
print(a[:,1])
# 将行和列转换，得到一个新的数组
print(a.transpose())