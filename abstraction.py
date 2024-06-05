                               #[ Abstraction of OOP in Python ]
#[ Hiding the details of a class and only showing the essential features to the user ]
class Car:
    def __int__(self):
        pass
    def start(self):
        self.clutch=True
        self.accelerat=True
        print("Car Started")
    def stop(self):
        self.clutch=False
        self.accelerat=False
        self.Break=True
        print("Car Stoped")

car1=Car()
car1.start()
















