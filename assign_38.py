def first_even(n):
    if n==1:
        print(2*n)
    else:
        first_even(n-1)
        print(2*n)
first_even(10)
print()

def first_even_rev(n):
    if n==1:
        print(2*n)
    else:
        print(2*n)
        first_even_rev(n-1)
first_even_rev(10)
print()

def sq_first(n):
    if n==1:
        print(n)
    else:
        sq_first(n-1)
        print(n**2)
sq_first(10)
print()

def cu_first(n):
    if n==1:
        print(n)
    else:
        sq_first(n-1)
        print(n**3)
cu_first(10)
print()

def rev_number(n):
    if(n==0):
        pass
    else:
        print(n%10,end='')
        rev_number(n//10)
rev_number(7589)