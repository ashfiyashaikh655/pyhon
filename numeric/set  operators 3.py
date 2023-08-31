#set operators
s1={1,2,3,4}
print('s1=',s1,len(s1))
s2=set()
print('s2=',s2,len(s2))

print()
print('add')
s2.add(1)
print('s2=',s2,len(s2))
s2.add(5)
s2.add(12)
s2.add(19)
print('s2=',s2,len(s2))

print()
print('copy')
s3=s2.copy()
print('s3=',s3,len(s3))

print()
print('discard')
s2.discard(19)
print('s2=',s2,len(s2))
s2.discard(400)
print('s2=',s2,len(s2))

print()
print('pop')
s4=s1.pop()
print('s1=',s1,len(s1),s4)
s5=s2.pop()
print('s2=',s2,len(s2))

print()
print('remove')
s1.remove(3)
print('s1=',s1,len(s1))
#s1.remove(17)
        

