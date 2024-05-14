def sumN(n):
    if n==1:
        return 1
    else:
        return n+sumN(n-1)
print(sumN(10))
print()

def sumoddN(n):
    if n==1:
        return 1
    else:
        return 2*n-1 + sumoddN(n-1)
print(sumoddN(10))
print()

def sumevenN(n):
    if n==1:
        return 2
    else:
        return 2*n+sumevenN(n-1)
print(sumevenN(10))
print()

def sumsquareN(n):
    if n==1:
        return 1
    else:
        return n*n+sumsquareN(n-1)
print(sumsquareN(10))
print()

def cubesum(n):
    if n==1: 
        return 1
    else:
        return n*n*n +cubesum(n-1)
print(cubesum(10))
print()


