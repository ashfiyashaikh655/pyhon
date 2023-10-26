'''The marks obtained by a student in 5 different
subjects are input through the keyboard. The student gets a
division as per the following rules:
Percentage above or equal to 60 - First division
Percentage between 50 and 59 - Second division
Percentage between 40 and 49 - Third division
Percentage less than 40 - Fail
Write a program to calculate the division obtained by the student'''

m1=int(input('m1:'))
m2=int(input('m2:'))
m3=int(input('m3:'))
m4=int(input('m4:'))
m5=int(input('m5:'))
total=m1+m2+m3+m4+m5
print('total=',total)
per=(total/500)*100
print('per=',per)
if per>=60:
    print('first division')
elif per>=50 and per<=59:
    print('second division')
elif per>=40 and per<=49:
    print('third division')
elif per<40:
    print('fail')
    
    

