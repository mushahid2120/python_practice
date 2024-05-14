class person:
    def __init__(self,a,n):
        self.age=a 
        self.name=n 
    def show(self):
        print(self.age,self.name,end=' ')
p=person(21,"Mushahid")

class circle:
    def __init__(self):
        self.radius=0
    def set(self,r):
        self.radius=r 
    def get(self):
        return self.radius
    def getArea(self):
        return self.radius**2*3.14
    def getcircum(self):
        return 3.14*self.radius*3.14

c=circle()
c.set(20)
#print(c.get(),c.getArea(),c.getcircum(),end=' ')

class Book:
    def __init__(self,b,t,p):
        self.bookid=b 
        self.title=t 
        self.price=p 
    def show(self):
        print(self.bookid,self.title,self.price,end=' ')
b=Book(1,"Rich dad poor dad",323.1)


class Team:
    def __init__(self):
        self.name=[]
    def input_names(self):
        for e in input().split(' '):
            self.name.append(e)
    def display(self):
        for e in self.name:
            print(e)
T=Team()
T.input_names()
T.display()