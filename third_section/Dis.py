from dis import dis
from unicodedata import name

a = {1}
dis(str(a))
print("-"*50)
dis("set([1])")
print("-"*50)

print(name(chr(97),""))