
'''def addition(a,b):
    add=a+b
    print('add:',add)

addition(1,6)
addition(5,9)

print()
def substraction(a,b):
    sub=a-b
    print('substraction:',sub)
    
substraction(14,8)
substraction(25,-9)

print()
def even_odd(num):
    if num%2==0:
        print(num,'even')
    else:
        print(num,'odd')

while True:
    num=int(input('num:'))
    even_odd(num)
'''
print()
def factorial(num):
    result=1
    for i in range(num,0,-1):
        result=result*i
    print('result:',result)

num=int(input('num:'))
factorial(num)
