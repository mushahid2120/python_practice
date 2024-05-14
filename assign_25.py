
l=[e*2 for e in range (1,int(input("Enter how many numer")),1)]
print(l)
print()

n=int(input("Enter a Number"))
a=-1
b=1
l=[]
while n:
    c=a+b
    a=b
    b=c
    l.append(c)
    n-=1
print(l)
print()


n=int(input("Enter a Number"))
l=[]
num=2
check=2
while num and n>len(l):
    while num**0.5>=check:
        if num%check==0:
            break
        check+=1
    else:
        l.append(num)
    check=2
    num+=1
print(l)

i=1
k=1
l=[]
l1=[]
while i<=2:
    while k<=3:
        l.append(int(input("Enter a Number:")))
        k+=1
    i+=1
    l1=[l1,l]

print(l1)

 
l1=[4,3,-6,-4,5]
l2=[5,-5,-3,3,56]
i=0
while i<len(l1):
    if(l1[i]<=0):
        l2.append(l1[i])
        del l1[i]
    else:
        i+=1

i=0
while i<len(l2):
    if(l2[i]>0):
        l1.append(l2[i])
        del l2[i]
    else:
        i+=1
print("l1=",l1)
print("l2=",l2)
