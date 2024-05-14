'''
def LCM(a,b):
    for e in range(a,a*b+1):
        if e%a==0 and e%b==0:
            return e
print(LCM(20,25))
print()

def count_word(a):
    ct=0
    for e in a:
        ct+=1
    return ct 
print(count_word("hello"))
print()

def primelist(a,b):
    l=[]
    for e in range(a,b+1):
        for k in range(2,e):
            if e%k==0:
                break
        else:
            l.append(e)
    return l 
print(primelist(40,100),end=' ')
print()

def fact_two(a,b):
    t=()
    for e in range(1,a):
        if a%e==0 and b%e==0:
            t1=(e,) 
            t=t+t1 
    return t 
print(fact_two(40,30),end=' ')
'''
def list_dict(l):
    d={}
    temp=[]
    for e in "abcdefghijklmnopqrstuvwxyz":
        for k in l:
            if k.startswith(e):
                temp.append(k)
        if len(temp)>0:
            d[e]=list(temp)
        temp.clear()
    return d 
print(list_dict([e for e in input("Enter a string/n").split(' ')]))