
                             #[ Tuples in Python ]

#[ Tuple are written in round brackets ]
tuple=("banana","apple","mango")
print(tuple)

print("_______________")

#[ Tuple Items - Data Types ]
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

#[ A tuple with strings, integers and boolean values ]
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

print("_______________")

#[ Access Tuple Items ]
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

print("_______________")

#[ Change Tuple Values (tuple change in VScode and other softwares not on pycham]
# x=('apple','banana','mango')
# y=list(x)
# y[1]="orange"
# x=tuple(y)
# print(x)
#[ Append Tuple Values (tuple appent in VScode and other softwares not on pycham]
# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("orange")
# x = tuple(y)
# print(x)

#[ This method is usefull of appent values in tuple ]
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

print("_______________")

#[ Unpacking tuple ]
fruits = ("apple", "banana", "cherry")
(apple, banana, cherry) = fruits
print(apple)
print(banana)
print(cherry)

#[ Using Asterisk* ]
'''[ If the number of variables is less than the number of values, you can add an * 
to the variable name and the values will be assigned to the variable as a list:]'''

x=('green','yellow','orange','blue','red')
(green,yellow,*orange)=x
print(x)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

print("_______________")

#[ Loop tuple ]
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("umar", "javed", "jutt")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

print("_______________")

#[ Join Tuples ]
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("umar", "javed", "jutt")
tuple3= tuple1+tuple2
print(tuple3)

num=(1,2,3,4,5)
x=num*2
print(x)

print("_______________")

#[ Tuple Methods ]
x=('apple','banana','cherry','banana')
print(x.count(banana))

x=('apple','banana','cherry','banana')
print(x.index(banana))
