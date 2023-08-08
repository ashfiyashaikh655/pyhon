#set operations
s1={1,2,3,4,5}
print('s1=',s1,len(s1))
s2={2,4,6,7,8}    
print('s2=',s2,len(s2))

print()
s3=s1.union(s2)
print('s3=',s3,len(s3))

print()
s4=s1.intersection(s2)
print('s4=',s4,len(s4))

print()
s5=s1.difference(s2)
print('s5=',s5,len(s5))
s6=s2.difference(s2)
print('s6=',s6,len(s6))

print()
s7=s1.symmetric_difference(s2)
print('s7=',s7,len(s7))

print()
print('add')
s1.add(11)
print('s1=',s1,len(s1))
s1.add(13)
print('s1=',s1,len(s1))
s1.add(15)
print('s1=',s1,len(s1))
s2.add(16)
print('s2=',s2,len(s1))
s2.add(17)
print('s2=',s2,len(s1))

s8=set()
print('s8=',s8,len(s8))  
s8.add(1)
print('s8=',s8,len(s8))
s8.add(13)
print('s8=',s8,len(s8))
s8.add(16)
print('s8=',s8,len(s8))
       




