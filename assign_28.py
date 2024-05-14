'''
l=['H','e','l','l','o','u',1,2,3,True]
i=0
while i<len(l)-1:
    if type(l[i])==int:
        i+=1
        #print(l[i])
    else:
        l.remove(l[i])
        #size-=1
        print(len(l))
print(l)

l=[2,3,4,5,3,2,3,5,4,5]
l.sort()
i=0
while i<len(l):
    print(l[i],"=",l.count(l[i]))
    i+=l.count(l[i])

l=[e for e in input("Enter list of string").split(' ')]
l.sort()
print(l)

l=[e for e in input("Enter a string sperated by space").split(' ')]
i=0
while i<len(l):
    if l.count(l[i])>1:
        print("First repeted string is",l[i])
        break
        i+=1
else:
    print("Not found")

'''
l=[e for e in input("Enter a string ").split(" ")]

for e in l:
    if e.endswith('s'):
        print(e)
