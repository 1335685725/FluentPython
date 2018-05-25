# 不可变的映射类型，d的内容可以通过MPT查看， 但是不能通过MPT修改
# dp是动态的，任何队d的修改都会反馈到dp上面

from types import MappingProxyType

d = {1: "A"}
d_proxy = MappingProxyType(d)
print(d_proxy.__repr__())
print(d_proxy[1])
# d_proxy[2] = "B"
d[2] = "b"
print(d_proxy)