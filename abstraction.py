                              #[ Abstraction of OOP in Python ]
#[ Hiding the details of a class and only showing the essential features to the user ]

from abc import ABC,abstractmethod
class Person(ABC):
    @abstractmethod
    def name(self):
        pass
class Person1_Data(Person):
    def name(self):
        print("Umar Javed")
class Person2_Data(Person):
    def name(self):
        print("Ali Ahmad")

p1=Person1_Data()
p2=Person2_Data()
p1.name()
p2.name()

print("_______________")


from abc import ABC,abstractmethod
class Student(ABC):
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    @abstractmethod
    def full_name(self):
        pass
class Student_1(Student):
    def full_name(self):
        return f'{self.fname} {self.lname}'
class Student_2(Student):
    def full_name(self):
        return f'{self.fname} {self.lname}'

s1=Student_1("Umar","Javed")
s2=Student_2("Usman","Ali")
print(s1.full_name())
print(s2.full_name())




















