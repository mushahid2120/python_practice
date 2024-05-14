#find factorial
fact=1
for e in range(int(input("Enter an  Number: ")),1,-1):
    fact=fact*e 
print(fact)
#count the number of digit
print()

n=input("Enter a Number")
count=0
for e in n:
    count+=1
print(count)

print()
#sum of the digit
n=int(input("Enter a Number:"))
sum=0
while n:
    sum=sum+n%10
    n//=10
print(sum)
print()
#find decimal to binary
sum=0
po=1
n=int(input("Enter a NUmber want to convert in Binary"))
while n:
    sum=sum+n%2*po
    po=10*po
    n//=2
print(sum)
#find decimal to octal
n=int(input("Enter a Number"))
sum=0
po=1
while n:
    sum=sum+n%8*po
    n//=8
    po=po*10
print(sum)