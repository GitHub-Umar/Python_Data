
                                #[ Multilevel Inheritance ]
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def all_info(self):
        return f"Person= Name: {self.first_name} {self.last_name}. age: {self.age}."

class Teacher1(Person):
    def __init__(self,first_name,last_name,age,job,rank):
        super().__init__(first_name,last_name,age)
        self.job = job
        self.rank = rank



    def all_info(self):
        return f"Teacher01= Name: {self.first_name} {self.last_name}. age: {self.age}. Job:{self.job}. Rank: {self.rank}."

class Teacher2(Teacher1):
     def __init__(self, first_name, last_name, age, job, rank,salary):
         super().__init__(first_name, last_name, age,job,rank)
         self.job = job
         self.rank = rank
         self.salary = salary

     def all_info(self):
        return f"Teacher02= Name: {self.first_name} {self.last_name}. age: {self.age}. Job:{self.job}. Rank: {self.rank}. Salary: {self.salary}"


person=Person('Umar','Javed',25)
teacher1=Teacher1('Ali','Ahmad',40,'Teaching','17th Grade')
teacher2=Teacher2('Ali','Ahmad',40,'Teaching','17th Grade',50000)
print(person.all_info())
print(teacher1.all_info())
print(teacher2.all_info())
