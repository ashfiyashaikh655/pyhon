list1=[]
print('list1',list1,len(list1))
print('append')
list1.append(14)
list1.append(19)
list1.append(7)
list1.append(-20)
list1.append(-4)
list1.append(14)
list1.append(18)
list1.append(-6)
list1.append(7)
list1.append(-15)
list1.append(-11)
list1.append(19)
print('list1',list1,len(list1))
print()
print('count')
a1=list1.count(7)
print('a1=',a1)
a2=list1.count(19)
print('a2=',a2)
a3=list1.count(1)
print('a3=',a3)
a4=list1.count(-15)
print('a4=',a4)

print('reverse')
list1.reverse()
print('list1',list1,len(list1))

print('sort')
list1.sort()
print('list1',list1,len(list1))

list1.sort(reverse=True)
print('list1',list1,len(list1))

print('index')
a5=list1.index(7)
print('a5=',a5)
a6=list1.index(-15)
print('a6=',a6)
a7=list1.index(18)
print('a7=',a7)

print('insert')
list1.insert(5,11)
print('list1',list1,len(list1))
list1.insert(3,7)
print('list1',list1,len(list1))
list1.insert(6,18)
print('list1',list1,len(list1))
list1.insert(9,-20)
print('list1',list1,len(list1))













