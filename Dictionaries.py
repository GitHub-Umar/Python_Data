                                #[ Dictionaries in Python ]
#[ Dictionary ]
dict = {
        "brand": "honda",
        "model": "civic",
        "year": 2024
       }
print(dict)

print("_______________")

#[ Dictionary Items ]
dict = {
        "brand": "honda",
        "model": "civic",
        "year": 2024
       }
print(dict['model'])

#[ Duplicates Not Allowed ]
dict = {
        "brand": "honda",
        "model": "civic",
        "year": 2024,
        "year": 1900
       }
print(dict)

print("_______________")

#[ Dictionary Length ]
dict = {
        "brand": "honda",
        "model": "civic",
        "year": 2024,
        "year": 1900
       }
print(len(dict))

print("_______________")


#[ Get Key ]
dict = {
        "brand": "honda",
        "model": "civic",
        "year": 2024
       }
print(dict.keys())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

print("_______________")

#[ Get values ]
dict = {
        "brand": "honda",
        "model": "civic",
        "year": 2024
       }
print(dict.values())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

print("_______________")

#[ Get items ]
dict = {
        "brand": "honda",
        "model": "civic",
        "year": 2024
       }
print(dict.items())

print("_______________")

#[ Change keys or values ]
dict = {
        "brand": "honda",
        "model": "civic",
        "year": 2024
       }
dict['year']=2022
print(dict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

print("_______________")

#[ Adding Items ]
dict = {
        "brand": "honda",
        "model": "civic",
        "year": 2024
       }
dict['color']='black'
print(dict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)

print("_______________")

#[ Remove Dictionary Items ]
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#[ popitem() method removes the last inserted item ]
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#[ del keyword removes the item with the specified key name ]
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

print("_______________")

#[ Nested Dictionaries ]
cars={
    'car1':{
        'brand':'honda',
        'model':'civic',
        'year':2022
    },
    'car2':{
        'brand':'toyota',
        'model':'altis',
        'year':2022
    }
}
print(cars)


car1={
        'brand':'honda',
        'model':'civic',
        'year':2022
}
car2={
        'brand':'toyota',
        'model':'altis',
        'year':2022
}
cars={
    "car1":car1,
    "car2":car2
}
print(cars)

print("_______________")

#[ Access Items in Nested Dictionaries ]
cars={
    'car1':{
        'brand':'honda',
        'model':'civic',
        'year':2022
    },
    'car2':{
        'brand':'toyota',
        'model':'altis',
        'year':2022
    }
}
print(cars['car1']["model"])
print(cars['car2']["model"])

print("_______________")

#[ Loop Through Nested Dictionaries ]
cars={
    'car1':{
        'brand':'honda',
        'model':'civic',
        'year':2022
    },
    'car2':{
        'brand':'toyota',
        'model':'altis',
        'year':2022
    }
}
for x,obj in cars.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])

print("_______________")

#[ Dictionary Methods ]
'''
clear()	    Removes all the elements from the dictionary
copy()	    Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary    
'''
#[ fromkeys() ]
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#[ get() ]

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

#[ popitem() ]
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)

#[ setdefault() ]
'''
The setdefault() method returns the value of the item with the specified key.
If the key does not exist, insert the key, with the specified value, see example below'''

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")
print(x)

















