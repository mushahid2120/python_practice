def isprime(a):
    for e in range(2,a):
        if a%e==0:
            return False
    else:
        return True

def deco_the_end(dhny):
    def the_end(dp):
        print("Good Bye")
        return dhny(dp)
    return the_end

@deco_the_end
def deco_happy_New_year(dcp):
    def print_hny(HF):
        print("Happy New Year")
        return dcp(HF)
    return print_hny

@deco_happy_New_year
def deco_co_prime(hcf):
    def co_prime(a,b):
        if isprime(a) and isprime(b):
            print("Two Numbers are co-prime")
        return hcf(a,b)
    return co_prime

@deco_co_prime
def HCF(a,b):
    for e in range(min(a,b),0,-1):
        if a%e==0 and b%e==0:
            return e 
    return 1





print(HCF(17,13))

def deco_is_prime(tellprime):
    def print_prime(n):
        for e in range(2,n):
            if isprime(e):
                print(e,end=' ')
        print()
        return tellprime(n)
    return print_prime

@deco_is_prime
def is_Prime(n):
    for e in range(2,n):
        if n%e==0:
            return False
    return True

print(is_Prime(41))

def deco_Right_Angle_triange(triagle):
    def Right_Angle(a,b,c):
        if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print("Right Angle Triangle")
        return triagle(a,b,c)
    return Right_Angle

@deco_Right_Angle_triange
def is_Triangle(a,b,c):
    if a+b>c or a+c>b or b+c>a:
        return True 
    return False

print(is_Triangle(4,3,5))