set1=set()
print('add element enter 1')
print('remove element enter 0')
while True:
    print()
    choice=int(input('choice:'))
    if choice==1:
        num=int(input('num1:'))
        set1.add(num)
        print('set1:',set1,len(set1))
    elif choice==0:
         num=int(input('num1:'))
         set1.discard(num)
         print('set1:',set1,len(set1))
    else:
        print('Enter valid data')
