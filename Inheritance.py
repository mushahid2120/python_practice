class Person: 
    def __init__(self,n,a):
        self.name=n
        self.age=a 
class Employee(Person):
    def __init__(self,n,a,s):
        super().__init__(n,a)
        self.salary=s 
    def show(self):
        print(self.name,self.age,self.salary,end=' ')
obj=Employee("Rahul",21,5000)


class Account:
    def __init__(self,ac,b,roi):
        self.AccountNumber=ac 
        self.Balance=b 
        Account.rate_of_Interest=roi 
class FixedDiposit(Account):
    def __init__(self,ac,b,roi,t):
        super().__init__(ac,b,roi)
        self.time=t 
    def show(self):
        print(self.AccountNumber,self.Balance,self.rate_of_Interest,self.time,end=' ')
    def SI(self):
        return self.Balance*self.rate_of_Interest*self.time/100


#super is function which return the intance object reference of parent class

class account:
    def __init__(self,b):
        self.balance=b 
    def withdraw(self,A):
        if b>=A:
            self.balanc-=A
            print("Available Balance is ",self.balance)
        else:
            print("No Balance")

class MinimumBalance(account):
    def __init__(self,b,MB):
        self.minbalance=MB
        super().__init__(b) 
    def withdraw(self,A):
        if self.minbalance<=self.balance-A:
            self.balance-=A 
            print("Available Balance is ",self.balance)
        else:
            print("Maintain minimum balance")

class polygon:
    def __init__(self,n,l):
        self.no_of_side=n 
        self.length=l
class Triangle(polygon):
    def __init__(self,l):
        super().__init__(3,l)
    def getArea(self):
        return (sum(self.length)-(max(self.length)+min(self.length)))*min(self.length)*0.5
T=Triangle([4,5,3])
print(T.getArea())



