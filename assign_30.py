'''
l=[3,4,2,3,4,2,2,5]
s={e for e in l}
print(s)


s={2,4,6,5,7,3,7,8,6,9,0}
s_even=set()
s_odd=set()
for e in s:
    if e%2:
        s_odd.add(e)
    else:
        s_even.add(e)
print(s_even,s_odd,end='\n')

'''
s={"Rahul","Sahil","Raj","Rohit","sid"}
t=()
l=[]
for e in s:
    for k in s:
        if e!=k:
            t=(e,k)
            l.append(t)
print(l)

'''
Hat={"Hamid","Ritesh","kuldip","Sid"}
shoes={"Ritesh","Rahul","Rohit","Sid"}
Hat_shoes=Hat.intersection(shoes)
print(Hat_shoes)

N=int(input("Enter a sum Number you want"))
t=()
l=[]
for e in range(1,7):
    for c in range(1,7):
        if e+c==N:
            t=(e,c)
            l.append(t)
print(l)
'''