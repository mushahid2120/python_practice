def firstodd(a):
    for e in range(1,a+1):
        print(e*2-1,end=' ')
firstodd(10)
print()
def firstprime(a):
    e=2
    while a:  
        for k in range(2,e):
            if e%k==0:
                break
        else:
            print(e,end=' ')
            a-=1
        e+=1
        if a==0:
            break
firstprime(5)
print()
 
def betprime(a,b):
    for e in range(a,b+1):
        for k in range(2,e):
            if e%k==0:
                break
        else:
            print(e,end=' ')
betprime(10,20)
print()

def Nfab(n):
    a=-1
    b=1
    c=0
    while n:
        c=a+b
        a=b 
        b=c
        print(c,end=' ')
        n-=1
Nfab(10)
print()

def factor(n):
    for e in range(2,n+1):
        if n%e==0:
            print(e,end=' ')
factor(21)