def createGenerator():
    mylist = range(5)
    for i in mylist:
        yield i*i

a_generator = createGenerator()

for i in a_generator:
    print(i)

a_generator = createGenerator()

for i in a_generator:
    print(i)
