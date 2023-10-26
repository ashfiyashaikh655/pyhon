list1=[10,20,30,40]
i1=iter(list1)
i2=iter(list1)
print(i1)
print('i1',i1.__next__())
print('i1',i1.__next__())
print('i2',i2.__next__())
print('i1',i1.__next__())
print('i1',i1.__next__())
print('i2',i2.__next__())

