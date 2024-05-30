                                            #[ Function in Python ]
#[ function ]
def my_function():
  print("Hello from a function")

my_function()

print("_______________")

#[ Arguments Information can be passed into functions as arguments ]
def my_function(fname):
  print(fname + " is a fruit")

my_function("apple")

print("_______________")

#[ Number of Arguments ]
def my_function(fname,lname):
  print(fname +" "+ lname)

my_function("umar","javed")

print("_______________")

#[ Arbitrary Arguments, *args ]
def my_function(*car):
  print(car[2] + ' is a best car')
my_function('civic','alto','audi')

print("_______________")

#[ Keyword Arguments ]
def my_function(car1, car2, car3):
  print("The car name is " + car2)

my_function(car1 = "civic", car2 = "altis", car3 = "audi")

print("_______________")

#[ Arbitrary Keyword Arguments, **kwargs ]
def my_function(**boy):
  print("His last name is " + boy["lname"])

my_function(fname = "umar", lname = "javed")

print("_______________")

#[ Default Parameter Value ]
def my_function(country = "pakistan"):
  print("I am from " + country)

my_function("pakistan")
my_function()

print("_______________")

#[ Passing a List as an Argument ]
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print("_______________")

#[ Return Values ]
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

print("_______________")


def my_function():
  list=['apple','banana','mango']
  list.reverse()
  print(list)
my_function()
my_function()


























