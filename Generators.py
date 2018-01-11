from threading import Thread


def myGenerator():
    myList = (x*x for x in range(25))
    for i in myList:
        yield i

gen1 = myGenerator()
print gen1
# print
# for i in gen1:
#     print(i)


print next(gen1)
print next(gen1)

