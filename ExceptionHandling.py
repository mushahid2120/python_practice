
'''class NegativeNotAllowed(Exception):
    def __init__(self,ErrorMsg):
        self.ErrorMsg=ErrorMsg
    def __str__(self):
        return self.ErrorMsg

try:
    N=int(input("Enter a Number: "))
    if N<0:
        raise NegativeNotAllowed("Negative Numbers is Not Allowed")
    fact=1
    for e in range(1,N+1):
        fact=fact*e 
    print(fact)
except ValueError:
    print("Please Enter Valid Number")
except NegativeNotAllowed:
    print('negative numbers is not allowed')
print("Hello")
'''

try: 
    a,b,c=int(input()),int(input()),int(input())
    if a>b>c:
        print("A is greater")
    elif a<b>c:
        print("B is greater")
    else:
        print("C is greatest")
except ValueError:
    print("Please Enter valid value")

