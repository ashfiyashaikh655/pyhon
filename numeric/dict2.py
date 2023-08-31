dict1={
    'school':"st ignatiu's high school",
    'boys':['zaid','areeb','kaif','ahad'],
    'girls':['lavizah','ashfiya','mariyam'],
    'age':22,
    'hobbies':['playing','listening music',
               ('travelling','reading')],
    
    }
print('dict1=',dict1,len(dict1))
a1=dict1['school']
print('a1=',a1)
a2=dict1['boys']
print('a2=',a2)
a3=dict1['boys'][-3]
print('a3=',a3)
a4=dict1['girls'][0][-4]
print('a4=',a4)
a5=dict1['age']
print('a5=',a5)
a6=dict1['hobbies']
print('a6=',a6)
a7=dict1['hobbies'][1]
print('a7=',a7)
a8=dict1['hobbies'][-1][-1]
print('a8=',a8)

print()
dict1['salary']=250000
dict1['address']='17/50 bdd chawl worli '
print('dict1=',dict1,(dict1))
