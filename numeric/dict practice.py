dict1={
    'name':['ashfiya','lavizah'],
    'mobile':[9372242638,9987252302],
    'age':20.6,
    'hobbies':['reading','writing','singing'],
    'skills':['python','java','.net','c++'],
    'school':{
            'ssc':'st.Ignatius high school',
            'hsc':'msb',
            'ty':'uom'
        },
    }
print('dict1=',dict1,len(dict1))
a1=dict1['name']
print('a1=',a1)
a2=dict1['mobile'][-1]
print('a2=',a2)
a3=dict1['age']
print('a3=',a3)
a4=dict1['hobbies'][-2]
print('a4=',a4)
a5=dict1['skills'][1]
print('a5=',a5)
a6=dict1['school']['ty']
print('a6=',a6)
a7=dict1['skills'][-1]
print('a7=',a7)

print()
dict2={
    'name':'Ashfiya',
    'age':20,
    'salary':85000,
    'skills':['python','java','html','c++'],
    'position':'jr.programmer'
    }
print('dict2=',dict2,len(dict2))
a1=dict2['name']
print('a1=',a1)
a2=dict2['age']
print('a2=',a2)
a3=dict2['skills'][2]
print('a3=',a3)
a4=dict2['salary']
print('a4=',a4)
a5=dict2['position']
print('a5=',a5)






