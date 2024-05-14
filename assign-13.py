'''
x=int(input("enter a number"))
if 1000>x>99:
    print("three digit number")
else:
    print("not a three digit number")

if(x>0):
    print("positive")
elif x<0:
    print("negative")
else:
    print("zero")

a=int(input("enter the Number of  a"))
b=int(input("enter the number of B"))
c=int(input("enter the numer of c"))

if b**2>4*a*c:
    print("equation has real and distinc value")
elif b**2==4*a*c:
        print("equation has real and not distinc value")
else:
    print("equation has neigther real nor distinc value")

a=int(input("enter a year"))
if a%100==0:
    if a%400==0:
        print("leap year") 
    else:
        print("not leap year")
elif a%4==0:
    print("leap year")
else:
    print("not leap year")

print("leap year" if a%400==0 else "not leap year" if a%100==0 else "leap year" if a%4==0 else "not leap year")
'''

a=int(input("enter the Number of  a"))
b=int(input("enter the number of B"))
c=int(input("enter the numer of c"))
if b<a>c:
    print(a)
elif a<b>c:
    print(b)
else:
    print(c)