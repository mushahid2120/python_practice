r=range(5,51,5)
for e in r:
    print(e,end=" ")
print()

N=int(input("Enter number of element"))
r=range(N,N*10+1,N)
for e in r:
    print(e,end=" ")
print()

M=int(input("Enter how much number of elemnets required"))
N=int(input("Enter the multiple you want"))
for e in range(N,N*M+1,N):
    print(e,end=" ")
print()

for e in range(N*10,N-1,-N):
    print(e,end=" ")
print()

N=int(input("Enter a  number want to print the Table"))
for e in range(N,N*10+1,N):
    print(e,end=' ')
print()

