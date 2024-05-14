'''
N=int(input("Enter How many even number you want "))
r=range(2,2*N+1,2)
for e in r:
    print(e,end=" ")
print()

N=int(input("Enter how many odd numbers you want"))
for e in range(1,2*N,2):
    print(e,end=" ")
print()

N=int(input("Enter the value of N"))
r=range(1,N+1,1)
for e in r:
    print(e,end=' ')
print()

N=int(input("enter the N for squares of numbers "))
for e in range(1,N+1,1):
    print(e**2,end=" ")
print()
'''
i=2
r=range(15,46,1)
for e in r:
    while e**0.5>=i:
        if e%i==0:
            break
        i+=1
       # print(e)
    else:
        print(e,end=' ')
    i=2
