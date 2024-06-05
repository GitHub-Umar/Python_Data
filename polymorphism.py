                                      #[ Polymorphism of OOP in Python ]
#[  describes the ability of something to have or to be displayed in more than one form. ]
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f'{self.brand} {self.model}'

car1=Car("Honda","Civic")
car2=Car("Toyota","Altis")
for x in (car1,car2):
    print(x.full_name())

















