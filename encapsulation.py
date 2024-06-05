                                   #[ Encapsulation of OOP in Python ]
              #[ Wrapping data and functions in a single unit and make data private ]

#[ Double underscor create a object private we cannot access directly ]
# class A:
#     a=10
#     __b=20 #Private
#
# obj=A()
# print(obj.a)
# print(obj.__b)


#[ we can access private obj using funtion( Constractor ) ]
class A:
    a=10
    __b=20 #Private
    def show(self,):
        print(self.__b)

obj=A()
obj.show()





















