'''
def firstN(n):
    if n==1:
        print(1)
    else:
        firstN(n-1)
        print(n)

firstN(10)

def first_revN(n):
    if n==1:
        print(n)
    else:
        print(n)
        first_revN(n-1)
first_revN(10)
'''
def first_oddN(n):
    if n==1:
        print(n)
    else:
        first_oddN(n-1)
        print(2*n-1)
first_oddN(10)
print()

def first_oddN_rev(n):
    if n==1:
        print(n)
    else:
        print(2*n-1)
        first_oddN_rev(n-1)
first_oddN_rev(10)
print()

def pri(n):
    if n==1:
        print("mysirg")
    else:
        print("mysirg")
        pri(n-1)
pri(10)