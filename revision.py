#LIST
 # l=[int(e) for e in input("Enter a number seperated by comas:\n").split(",")]

# print(sum(l))
# print(sum(l)/len(l))
'''
l1=[e*e for e in l]
print(l1)

l.sort(reverse=True)
print(l)

print(l[1::2])

N=int(input("Enter a number:\n"))
l=list(range(2,2*N+1,2))
print(l)
'''
 #N=int(input("Enter a number:\n"))
'''
x=-1
y=1
z=0
l=[]
for e in range(1,N+1):
    z=x+y
    x=y
    y=z
    l.append(z)
print(l)
n=2
def isprime():
    global n 
    for e in range(2,n):
        if n%e==0:
            return False
    else:
        return True 
def nextprime():
    global n 
    n+=1
    while not isprime():
        n+=1
    return n 
l=[nextprime() for e in range(1,N+1)]
print(l)

m1=[]
m2=[]
m3=[]
for e in range (1,4):
    m1.append([int(e) for e in input("Enter a number for m1:\n").split(",")])

for e in range (1,4):
    m2.append([int(e) for e in input("Enter a numbers for M2:\n").split(",")])

for e in range(0,3):
    m3.append([m1[e][0]+m2[e][0],m1[e][1]+m2[e][1],m1[e][2]+m2[e][2]])
print(m1,m2,m3,sep="\n")

l=[int(e) for e in input("Enter a number").split(" ")]
pos=[]
nopos=[]
for e in l:
    pos.append(e) if e>0 else nopos.append(e)
print(pos,"\n",nopos)
'''
# STRING
s="This is my   new  files of python  "
'''
print(s.isdigit())
print('d' in s)

count=0
for e in s:
    if (e in "aeiouAEIOU"):
        count+=1
print(count)

l=s.split(" ")
while "" in l:
    l.remove("")
print(l,s)
print(len(l))
print("b" in ["a",'c'])

print(s[::-1])


s="All is possible:"
s=" ".join(s.split(" ")[::-1])
print(s)


s="My 1 house in streer 345 another is 456"
l=[]
for e in s.split(" "):
    if(e.isdigit()):
        l.append(e)
print(l)

a='nitin'
if a==a[::-1]:
    print("palandrome")
else:
    print("Not a palandrome")

s="mushahid"
s=s.upper()
print(s)

maxlength=0
s='Life is too short and beatiful'
for e in s.split(" "):
    if maxlength<len(e):
        maxlength=len(e)
print(maxlength)
'''

#list and string
'''
l=['abc',5,4,6.4,7.5,4j+2,True]
i=0
while len(l)>i:
    if not type(l[i])==int:
        l.remove(l[i])
    else:
        i+=1
print(l)


l=[3,45,2,1,4,6,555.5]
i=0
for e in l:
    if l.index(e)==i:
        print(e,'=',l.count(e))
    i+=1
'''
#l=["Rahul","Rohits","Sidharth"]
'''' 
l.sort()
print(l)
'''
'''
for e in l:
    if l.count(e)>1:
        print(e)
        break

count=0
for e in l:
    if e[-1]=='s':
        count+=1
print(count)
'''

#Tuple

#l=[3,4,6,2,43,32,3,2,3]

#t=tuple(l)
#print(t)

#print(t[::-1])
'''
temp=[]
l1=[]
l=['hello','hi','how','diet']
for e in 'abcdefghijklmnopqrstuvwxyz':
    for k in l:
        if k.startswith(e):
            temp.append(k)
    if len(temp)>0:
        l1.append(tuple(temp))
    temp=[]

print(l1)


l=['a','t','A']
l1=[]
for e in l:
    l1.append((e.upper(),ord(e)))
print(l1)


t=(3,5,3,2,4,5,74,43,3)
sum=0
for e in t:
    if e%2:
        sum=sum+e
print(sum)

l=[3,4,2,5,4,7,6,5]
s=set(l)
print(s)



s={3,3,52,53,43.33,22}
sodd=set()
seven=set()
for e in s:
    if e%2:
        sodd.add(e)
    else:
        seven.add(e)
print(sodd,seven,sep=' ')

s={'Rahul',' Avi' ,' sid' ,' Akhi',' Vikas'}
for e in s:
    for k in s:
        if(e!=k):
            print(e,k)
            print()




hs={3,4,25,2,12,4,5,2,3,4,5}
rs={3,42,2,34,2,1,3,4,3,2,4,3,2}
s=hs.intersection(rs)
print(s)


N=int(input('Enter a numbers\n'))

d={e:e**2 for e in range(1,N+1)}
print(d)

d={1:"Rahul",7:"sid",9:"Hello"}
k=sorted(d)
print(k)


d={}
for e in range(1,5):
    d[input("Enter players Name:\n")]=tuple([int(e) for e in input('matched palyed:\n,total run\n,half centuries\n Centuries\n').split(",")])
print(d)

l=["Delhi","Mumbai","Lucknow","Deoghar","Maharastra"]
d={}
l1=[]
for e in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for k in l:
        if k.startswith(e):
            l1.append(k)
    if len(l1)>0:
            d[e]=l1  
    l1=[];
        
print(d)
'''
# LAMBDA
print((lambda a:False if a%2 else True)(5))
fabnth=lambda n:1 if n==0 or n==1 else fabnth(n-1) + fabnth(n-2)
print(fabnth(5))

print((lambda r:r*3.14*r)(22))

hcf=lambda a,b: min(a,b) if max(a,b)%min(a,b)==0 else hcf(max(a,b)%min(a,b),min(a,b))
print(hcf(12,16))