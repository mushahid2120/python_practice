#print((lambda a:a%2==0)(2))

#fabonaci series pending
f=lambda n:n if n==0 or n==1 else f(n-2)+f(n-1)
#print(f(6))
 
#print((lambda r:r*r*3.14)(32))

#find HCF pending......
h=lambda a,b:min(a,b) if min(a,b)==1 or max(a,b)%min(a,b)==0 else h(max(a,b)%min(a,b),min(a,b))
print(h(12,24))
#print((lambda l:len(l))([4,3,5,2,4,5,6]))

prime=lambda n:n if n==1 else prime(n-1)+Nthprime(n)
Nthprime =lambda n:n if n==2 else nextprime(Nthprime(n-1))
def nextprime(n):
    n+=1
    while not isprime(n):
        n+=1
    return n
def isprime(n):
    for e in range(2,n):
        if n%e==0:
            return False
    return True

#print(prime(10))