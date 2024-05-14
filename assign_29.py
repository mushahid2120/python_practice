'''
l=[e for e in input("Enter a string").split(' ')]
t=()
for e in l:
    t1=(e,)
    t=t1+t
print(t)

t=(2,4,2,1,5,6,3,56,5)
print(t[::-1])

s=[e for e in input("Enter the string").split(' ')]
s.sort()
i=0
l=[]
result=[]
#print(s)
while i<len(s):
    k=i+1
    l.append(s[i])
    while k<len(s) and l[0].startswith(s[k][0]):
        l.append(s[k])
        k+=1
    result.append(tuple(l))
    i=k
    l.clear()
print(result)
'''
l=[e for e in input("Enter the string").split(' ')]
l.sort()
temp=[]
result=[]
for e in "abcdefghijklmnopqrstuvwxyz":
    for k in l:
        if k.startswith(e):
            temp.append(k)
    if len(temp)>0:
        result.append(tuple(temp))
    temp.clear()
print(result)

'''
l=[]
for e in input("Enter a string"):
    e=e.upper()
    t=(e,ord(e))
    l.append(t)
print(l)

s=0
t=(3,5,3,1,6,3,7,8,5,4,10)
for e in t:
    if e%2:
        s=e+s
print(s)
'''