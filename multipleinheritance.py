                                   #[ Multiple Inheritance ]
class A:
    def class_A(self):
        return f'A'

class B:
    def class_B(self):
        return f'B'

class C(A,B):
    pass
instance_c=C()
print(instance_c.class_A())
print(instance_c.class_B())























