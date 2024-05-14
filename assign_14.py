'''
a=int(input("enter a number: "))
match a:
    case a if a<0:
        print("number is negative")
    case a if a>0:
        print("number is positive")
    case _:
        print("number is zero")
print("choose an option \n 1.odd-even\n 2.positive-negative \n 3.simple interest \n 4.find the roots of quadratic equation")
z=int(input())
match z:
    case 1:
        x=int(input("enter a number"))
        if x%2:
            print("odd")
        else:
            print("even")
    case 2:
        x=int(input("enter a number"))
        if x>0:
            print("positive")
        else:
            print("negative")
    case 3:
        p=int(input("enter principle"))
        r=int(input("rate"))
        t=int(input("time"))
        print(p*t*r/100)
    case 4:
        a=int(input("enter the Number of  a"))
        b=int(input("enter the number of B"))
        c=int(input("enter the numer of c"))

        if b**2>4*a*c:
            print("equation has real and distinc value")
        elif b**2==4*a*c:
                print("equation has real and not distinc value")
        else:
            print("equation has neigther real nor distinc value")
    case _:
        print("enter option")
    

a=eval(input("enter a number: "))
match a:
    case a if type(a)==int:
        print("Monday")
    case a if type(a)==float:
        print("Tuesday")
    case a if type(a)==complex:
        print("wednesday")
    case a if type(a)==bool:
        print("Thrusday")
    case _:
        print("invalid type")
    '''
a=input("enter a string")
match a:
    case a if a in "mysirg":
        print("one")
    case a if a in "education":
        print("two")
    case a if a in "services":
        print("three")


