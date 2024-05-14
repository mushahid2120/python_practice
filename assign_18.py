for x in "abcdefghijklmnopqrstuvwxyz":
    print(x," ",ord(x))

print()
for x in "abcdfjguemABCEYUIIO":
    if x in "AEIOUaeiou":
        print(x)

count=0
for x in "hello woerd I am here":
    if x in " ":
        count+=1
print(count)

print()
a=65743657
z=""
for x in str(a):
    if x not in z:
        print(x)
        z=z+x

print()
a=4563
count=0
for x in str(a):
    count+=1 
print("count=",count)