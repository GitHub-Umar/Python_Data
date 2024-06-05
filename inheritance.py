                                 #[ Inheritance in Python ]

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def all_info(self):
        return f"Name: {self.first_name} {self.last_name}. age: {self.age}."

class Teacher(Person):
    def __init__(self,first_name,last_name,age,job,rank):
        super().__init__(first_name,last_name,age)
        self.job=job
        self.rank=rank

    def all_info(self):
        return f"Name: {self.first_name} {self.last_name}. age: {self.age}. Job:{self.job}. Rank: {self.rank}."



person=Person('umar','javed',25)
teacher=Teacher('ali','ahmad',40,'Teaching','17th Grade')
print(person.all_info())
print(teacher.all_info())

print("_______________")


















