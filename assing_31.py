'''
d={x:x**2 for x in range(1,7)}
print(d)

d={3:'heloo',1:'mys ',34:'hi',59:'hiiii'}
l=sorted(d.values(),reverse=True)
print(l)


d={}
for e in range(1,6):
    s=input("Enter name of the players")
    t=(int(input("Enter a matched played")),int(input("Enter a run")),int(input("Enter half centuries")),int(input("Enter half centuries")))
    d[s]=t 
print(d)


Batch={2:5,3:7,27:2,279:1,25:20}
b_max=2
for e in Batch:
    if(Batch[e]>b_max):
        b_max=e
print(Batch[b_max])
'''

temp=[]
d={}
s=[e for e in input("Enter a string").split(' ')]
for e in "abcdefghijklmnopqrstuvwxyz":
    for k in s:
        if k.startswith(e):
            temp.append(k)
    if len(temp)>0:
        d[e]=tuple(temp)
    temp.clear()
print(d)