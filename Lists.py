                             #[ Lists in Python ]

#[ Lists are created using square brackets and list contain differnet data types ]
list1 = ['apple','banana','cherry']
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(list4)

print("_______________")

#[ list() Constructor use the list() constructor when creating a new list ]
mylist=list(('apple','banana','mango'))
print(mylist)

print("_______________")

#[ Access List Items access them by referring to the index number ]
thislist = ["apple", "banana", "cherry"]
print(thislist[2])

print("_______________")

#[ Change Item Value ]
list = ["apple", "banana", "cherry"]
list[2]='mango'
print(list)

#[ Change a Range of Item Values [
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["mango", "watermelon"]
print(thislist)

print("_______________")

#[ Add List Items ]
#[ Insert Items ]
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#[ Append ]
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#[ Extend List ]
list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "watermelon"]
list1.extend(list2)
print(list1)

#[ Add Any Iterable ]
list = ["apple", "banana", "cherry"]
tuple = ("kiwi", "orange")
list.extend(tuple)
print(list)

print("_______________")

#[ Remove Specified Item ]
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#[ Remove Specified Index ]
thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print("_______________")


#[ Loop Through a List ]
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print("_______________")


#[ Loop Through the Index Numbers ]
thislist = ["mango", "watermelon", "orange"]
for i in range(len(thislist)):
  print(thislist[i])

print("_______________")


#[ Using a While Loop of list ]
list = ["apple", "banana", "cherry"]
i = 0
while i < len(list):
  print(list[i])
  i = i + 1

print("_______________")

#[ Looping, Using List Comprehension. A short hand for loop that will print a list ]
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#[ List Comprehension ]
list=['apple','banana','cherry']
newlist=[]
for x in list:
    if 'a' in x:
        newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#[ For list of numbers ]
list=[ x+1 for x in range(10) if x < 5]
print(list)

#[ For upper/lower case ltters ]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

fruits = ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
newlist = [x.lower() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

print("_______________")

#[ Sort Lists  alphabetically and numerically Ascending order]
list = ["orange", "mango", "kiwi", "pineapple", "banana"]
list.sort()
print(list)

list = [1, 5, 6, 8, 2]
list.sort()
print(list)

#[ Sort Lists  alphabetically and numerically Dscending order]
list = ["orange", "mango", "kiwi", "pineapple", "banana"]
list.sort(reverse=True)
print(list)

list = [1, 5, 6, 8, 2]
list.sort(reverse=True)
print(list)

print("_______________")

#[ Customize Sort Function Sort the list based on how close the number is to 50 ]
def myfunc(n):
  return abs(n - 50)
list = [100, 50, 65, 82, 23]
list.sort(key = myfunc)
print(list)

print("_______________")

#[ Case sensitive sorting can sort capital letters first than other ]
list = ["banana", "Orange", "Kiwi", "cherry"]
list.sort()
print(list)

#[ case-insensitive sort ]
list = ["banana", "Orange", "Kiwi", "cherry"]
list.sort(key = str.lower)
print(list)

print("_______________")

#[ Copy Lists ]
list = ["apple", "banana", "cherry"]
mylist = list.copy()
print(mylist)

print("_______________")

#[ Join Lists ]
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["u", "m" , "a","r"]
list2 = [1, 9, 9,7]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
