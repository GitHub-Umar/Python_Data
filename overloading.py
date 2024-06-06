                          #[ Implement Overloading in Python ]

class Addition:
    def __add__(self,x=None,y=None,z=None):
        if x!=None and y!=None and z!=None:
            print(x+y+z)
        elif x!=None and y!=None:
            print(x+y)
        else:
            print("invalid entery")
a1=Addition()
a1.__add__(2,3)
a1.__add__(2,3,5)

print("_______________")

#[ Operator Overloading ]
class Number:
    def __init__(self,x):
        self.x=x
    def __add__(self, other):
        return self.x + other.x

n1=Number(10)
n2=Number(20)
print(n1+n2)
























