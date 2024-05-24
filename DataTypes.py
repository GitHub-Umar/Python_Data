
                            #[ Data Types in Python. ]

#[ Python built-in-datatypes ]
'''
Text Type:	      str
Numeric Types:	  int, float, complex
Sequence Types:	  list, tuple, range
Mapping Type:	  dict
Set Types:	      set,frozenset
Boolean Type:	  bool True,False
Binary Types:	  bytes, bytearray, memoryview
None Type:	      NoneType
'''
#[ Check Datatype of Variables ]
a='umar'
b=1
c=0.1
d=1j
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("_______________")

x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = {"name" : "John", "age" : 36}
print(type(x))
x = {"apple", "banana", "cherry"}
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
x = bool(1)
print(type(x))
x=True and False
print(type(x))
x = bytes(2)
print(type(x))
print(x)
x = bytearray(5)
print(type(x))
print(x)
x = memoryview(bytes(2))
print(type(x))
print(x)