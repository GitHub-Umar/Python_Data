                                 #[ Variables in Python ]

#[ Assign value to a variable. ]
x=1
y="umar"
print(x)
print(y)
print(type(x))
print(type(y))

print("_______________")

#[ Casting ]
x=str(2)
y=int(3)
z=float(3.0)
print(x)
print(y)
print(z)

print("_______________")

#[ Legal Variables ]
myvar = "umar"
my_var = "ali"
_my_var = "ahmad"
myVar = "waqas"
MYVAR = "saad"
myvar2 = "abdullah"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

print("_______________")

#[ Assign a values to multiple variables in one line ]
a,b,c="apple","banana","cherry"
print(a,b,c)
print(a)
print(b)
print(c)

print("_______________")

#[ Assign a same value to multiple variables ]
x=y=z="umar"
print(x,y,z)
print(x)
print(y)
print(z)

print("_______________")

#[ Unpacking a list ]
fruits=['a:apple','b:banana','c:cherry']
a,b,c=fruits
print(a,b,c)
print(a)
print(b)
print(c)

print("_______________")

#[ use + operator for to output multiple variable ]
x="I "
y="am "
z="Umar"
print(x+y+z)

print("_______________")

#[ output of multiple variables ]
x=1
y="umar"
print(x,y)

print("_______________")

#[ Global Variables ]
x='Umar.'
def myfunc():
    print('My name is '+x)
myfunc()

print("_______________")


x='Bahawalpur.'
def myfunc():
    x = 'Umar.'
    print('My name is ' + x)
myfunc()
print('I am from '+x)

print("_______________")

#[ global keyword, the variable belongs to the global scope ]
def myfunc():
  global x
  x = "fantastic language."
myfunc()
print("Python is " + x)

print("_______________")

#[ Changing value of a global variable ]
x = "fantastic"
def myfunc():
  global x
  x = "awesome"
myfunc()
print("Python is " + x)

print("_______________")
