def countvol(s):
    ct=0
    for e in s:
        if e in "aeiouAEIOU":
            ct+=1
    return ct 

l=map(countvol,["hello",'hi','md','jack'])
print(list(l))

def nuofdigit(n):
    ct=0
    for e in str(n):
        ct+=1
    return ct
l=map(nuofdigit,[276,432,5432,65,7,23432])
print(list(l))

def intvalue(n):
    try:
            return int(n)
    except:
        pass
f=filter(intvalue,['32',3,21,'hello',4.2,'mushahid'])
print(list(f))

def HCF(a,b):
    for e in range(min(a,b),0,-1):
        if a%e==0 and b%e==0:
            return e 
from functools import reduce
r=reduce(HCF,[15,5,30,50])
print(r)