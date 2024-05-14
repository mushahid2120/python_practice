def average(*t):
    return sum(t)/len(t)
print(average(30,50,40))

def greatest(*t):
    return max(t)
print(greatest(3,45,3,2,3,34,2,333))

def oddevn(*l):
    odd=[]
    even=[]
    for e in l:
        if e%2==0:
            even.append(e)
        else:
            odd.append(e)
    return [even,odd]
print(oddevn(1,2,38,8,7,5,6,87,4))

def maxlensalary(*t):
    max=-1
    l=[]
    for e in t:
        if len(e)>max:
            max=len(e)
            l=[e]
        elif len(e)==max:
            l.append(e)

    return l 
print(maxlensalary("md","mushahid","ansari","firozerr"))

def filterprime(*t):
    l=[]
    for e in t:
        for k in range(2,e):
            if e%k==0:
                break
            else:
                l.append(e)
    return l 
print(filterprime(3,45,2,1,33,4,5,3,2211,3))