list1=[
      'ashfiya',('python','java','html','c++','.net',[3.11,3.12,(1990,2020)]),
      'lavizah',('python','java','html','c++','.net',[7.12,7.16,(2020,2023)]),
      ]
print('list1=',list1,len(list1))
a1=list1[-1][-5]
print(a1)
a2=list1[-1][-1][-1]
print(a2)
a3=list1[-1][-1][-2]
print(a3)
a4=list1[-1][-1][-1][-1]
print(a4)
a5=list1[-3][-1][-1][-2]
print(a5)
a6=list1[-3][-1][-2]
print(a6)

print()
print('slicing')
a1=list1[1][1:5][1:3]
print(a1)
a2=list1[3][:4][:2][-1]
print(a2)
a3=list1[2][2:5]
print(a3)
a4=list1[3][3]
print(a4)
a5=list1[-3][4][-1]
print(a5)
a6=list1[-3][-1][-2]
print(a6)
