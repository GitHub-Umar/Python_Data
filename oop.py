                                 #[ Object Oriented Programming in PYthon ]

class Student:
    def __init__(self,first_name,last_name,roll_num,):
        self.first_name=first_name
        self.last_name=last_name
        self.roll_num=roll_num

    def all_info(self):
        return f"Name: {self.first_name} {self.last_name}. Roll num: {self.roll_num}"


s1=Student('Umar','Javed',48)
s2=Student('Ali','Ahmad',50)
print(s1.first_name)
print(s1.last_name)
print(s1.roll_num)
print(s1.all_info())
print(s2.all_info())


print("_______________")








































