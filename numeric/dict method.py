dict1={
    'name':'lavizah',
    'age':20,
    'skills':['python','java','c++'],
    'job':'software programmer',
    'salary':'870000'
    }
print('dict1=',dict1,len(dict1))
a1=dict1.keys()
print('a1=',a1)
a2=dict1.values()
print('a2',a2)
a3=dict1.items()
print('a3=',a3)

print()
a4=dict1.get('name')
print('a4=',a4)
a5=dict1.get('age')
print('a5=',a5)
a6=dict1.get('skills')
print('a6=',a6)
a7=dict1.get('job')
print('a7=',a7)
a8=dict1.get('salary')
print('a8=',a8)

print()
a9=dict1.pop('name')
print('a9=',a9)

print()
a10=dict1.popitem()
print('a10',a10)
a11=dict1.popitem()
print('a11',a11)

print()
a12=dict1.setdefault('skills',['python','java','c++'])
a13=dict1.setdefault('salary',870000)
print('dict1=',dict1,len(dict1))








