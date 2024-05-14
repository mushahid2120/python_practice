'''
s=input("Enter a sting seperated by space")
s=' '.join(s.split(' ')[::-1])
print(s)



l1=[]
s=input("Enter a string")
for e in s.split(' '):
    try:
        l1.append(float(e))
    except:
        pass
print(l1)
'''
'''
s=input()
print("palandrom" if s==s[::-1] else "not a palandrom")
'''

s=input("Enter a string")
maxword=0
for e in s.split(' '):
    if len(e)>maxword:
        maxword=len(e)
print(maxword)