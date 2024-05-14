'''
print(not ("Hello".isdigit()))

print()

a=input("Enter a sring")
print(a in "Mysirg")
'''
'''
s=input("Enter a string")
count=0
for e in s:
    if e in "AEIOUaeiou":
        count+=1
print(count)
'''

s=input("Enter a String")
count=0
for e in s.split(' '):
    if e!='':
        count+=1
        print(e)
print(count)


s=input("Enter a string")
s=s[::-1]
print(s)
