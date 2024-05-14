#question 1 is pending

class Person:
    def __init__(self,n,a):
        self.Name=n 
        self.Age=a 
class Student(Person):
    def __init__(self,n,a,r):
        Person.__init__(self,n,a)
        self.roll_no=r 
    def show(self):
        print(self.Name,self.Age,self.roll_no,end=' ')
class Teacher(Person):
    def __init__(self,n,a,s):
        Person.__init__(self,n,a)
        self.Subject=s
    def show(self):
        print(self.Name,self.Age,self.Subject,end=' ')

obj=Student("Mushahid",22,19000719072)
obj.show()
obj=Teacher("Raju",21,122000003665)
obj.show()

class Time:
    def __init__(self,h,m,s):
        self.hours=h
        self.min=m
        self.sec=s 
    def __gt__(self,obj):
        if self.hours>obj.hours:
            return True 
        elif self.min>obj.min:
            return True 
        elif self.sec>obj.sec:
            return True 
        return False 
    def __add__(self,obj):
        return Time(self.hours+obj.hours,self.min+obj.min,self.sec+obj.sec)
obj1=Time(3,20,10)
obj2=Time(2,12,34)
print(obj1>obj2)

class Result:
    def __init__(self,att,r,w):
        self.attempt=att
        self.wrong=w 
        self.right=r 
    def __add__(self,obj):
        obj1=Result(0,0,0)
        obj1.attempt=self.attempt+obj.attempt
        obj1.wrong=self.wrong+obj.wrong
        obj1.right=self.right+obj.right
        return obj1 
print((Result(5,3,2)+Result(10,4,6)).attempt)

class Matrix:
    def __init__(self,r,c):
        self.row=r 
        self.column=c 
        self.lt=[]
        l1=[]
        for e in range(0,r):
            for k in range(0,c):
                l1.append(0) 
            self.lt.append(list(l1))
            l1.clear()

    def inp(self):
        for e in range(0,self.row):
            for k in range(0,self.column):
                self.lt[e][k]=int(input())
    def show(self):
        for i in self.lt:
            for j in i:
                print(j,end=' ')
            print()
    def __add__(self,obj):
        temp=Matrix(self.row,self.column)
        for e in range(0,self.row):
            for k in range(0,self.column):
                temp.lt[e][k]=self.lt[e][k]+obj.lt[e][k]
        return temp
m1=Matrix(3,3)
m2=Matrix(3,3)
m1.show()
m1.inp()
m1.show()
m2.show()
m2.inp()
(m1+m2).show()
