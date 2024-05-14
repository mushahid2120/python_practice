def check(a):
    return a%2==0
print(check(32))

def greater(a,b,c):
    if a>b:
        return (a if a>c else c)
    else:
        return (b if b>c else c)
print(greater(7,4,9))

def check_Prime(a):
    for e in range(2,9):
        if a%e==0:
            return False
    else:
        return true
print(check_Prime(3))

def check_leapyear(a):
    if a%100==0:
        return True if a%400==0 else False
    else:
        return True
print(check_leapyear(2001))

