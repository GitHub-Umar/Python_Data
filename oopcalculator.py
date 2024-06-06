                     #[ Calculator using OOP in Python ]
class Calculator:
    def __init__(self,num1,mode,num2):
        self.num1=num1
        self.mode=mode
        self.num2=num2
    def add(self):
            return self.num1 + self.num2
    def subtract(self):
            return self.num1 - self.num2
    def multiple(self):
            return self.num1 * self.num2
    def divide(self):
            return self.num1 / self.num2
    def mode(self):
            return self.num1,self.num2

num1=float(input("Enter a first num: "))
mode=input("Chose an Operation(+,-,*,/): ")
num2=float(input("Enter your age: "))
cal=Calculator(num1,mode,num2)
if mode =="+":
    print(cal.add())
elif mode =="-":
    print(cal.subtract())
elif mode =="*":
    print(cal.multiple())
elif mode=="/":
    print(cal.divide())
else:
    print("Invalid Entery")

























