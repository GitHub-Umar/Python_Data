                                                #[ For loop in Python ]
#[ for loop ]
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("_______________")

#[ Looping Through a String ]
for x in "banana":
  print(x)

print("_______________")

#[ break ststement in for loop ]
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("_______________")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("_______________")

#[ continue Statement in for loop ]
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("_______________")

#[ range() Function ]
for x in range(6):
  print(x)

print("_______________")
#[ Using the start parameter ]
for x in range(2, 6):
  print(x)

print("_______________")

#[ range with sequence ]
for x in range(2,15,2):
  print(x)

print("_______________")

#[ Else in For Loop ]
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("_______________")

#[ loop breaking in for loop ]
for x in range(6):
  if x==4: break
  print(x)
else:
  print("Finally finished!")

print("_______________")

#[ Nested Loops in for loop ]
quantity=["2kg"]
fruits=['apple','banana','mango']
for x in quantity:
  for y in fruits:
    print(x,y)




























