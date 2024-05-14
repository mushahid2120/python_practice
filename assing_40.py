def sumdigit(n):
    if n==0:
        return 0
    else:
        return n%10 +sumdigit(n//10)
#print(sumdigit(3452))
print()

#factorial pending
def fact(n):
    if n==1:
        return 1 
    else:
        return n*fact(n-1)
print(fact(5))

def fab(n):
    if n==-2:
        return -1
    elif n==-1:
        return 1
    else:
        k=fab(n-2)+fab(n-1)
        print(k,end=' ')
        return k

print(fab(5))


def bin(n):
    if(n==1 or n==0):
        return n
    else:
        return bin(n//2)*10 + n%2
#print(bin(25))
print()

def octa(n):
    if(n>=0 and n<=7):
        return n
    else:
        return octa(n//8)*10+n%8
#print(octa(12))