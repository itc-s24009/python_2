print(2.3)
print(1,2,3,4.5,6,78)
print('abc')
name = input('お名前は？')
print(name)
print(len(name))

name_iter = iter(name)
next(name_iter)
next(name_iter)
next(name_iter)
next(name_iter)
print(next(name_iter))


