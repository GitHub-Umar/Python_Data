# 1 Write a Python function to add two numbers.
def addition(num1,num2):
    return num1+num2
print(addition(2,3))

print("_______________")

# 2 Create a function that takes a string as input and returns its length.
def len_string(input_string):
    return len(input_string)
input_string="umar"
print(len_string(input_string))

print("_______________")

# 3 Write a function to check if a number is even or odd.
def even_odd(num):
    if num %2==0:
        return "even"
    else:
        return "odd"
print(even_odd(7))

print("_______________")

# 4 Create a function that takes a list of numbers and returns the sum of all the numbers in the list.
def list(numbers):
    return sum(numbers)
numbers=[1,2,3,4]
print(list(numbers))

print("_______________")

# 5 Write a function to find the maximum of two numbers.
def max(num1,num2):
    if num1>num2:
        return "num:1"
    else:
        return "num:2"
print(max(2,3))

print("_______________")

# 6 Create a function that takes a list of numbers and returns the average.
def average(numbers):
    total=sum(numbers)
    return total/len(numbers)
numbers=[1,2,3,4,5]
print(average(numbers))

print("_______________")

# 7 Create a function that takes a string and returns it in uppercase.
def upper_string(name):
    return name.upper()
name='umar'
print(upper_string(name))

print("_______________")

# 8 Create a function that takes a list of numbers and returns a new list with only the even numbers.
def get_even_num(list_numbers):
    new_list=[]
    for num in list_numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
list_numbers=[1,2,3,4,5,6,7,8]
print(get_even_num(numbers))

def get_even_num(numbers):
    new_list=[num for num in numbers if num%2==0]
    return new_list
numbers=[12,13,14,15,16]
print(get_even_num(numbers))

print("_______________")

# 9 Write a function to reverse a string.
def reverse_string(name):
    return name[::-1]
name="remu"
print(reverse_string(name))

print("_______________")

# 10 Create a function that takes a list of numbers and returns the product of all the numbers in the list.
def product_num(numbers):
    product=1
    for num in numbers:
        product*=num
    return product
numbers=[1,2,3,4,5]
print(product_num(numbers))

print("_______________")

# 11 Write a function to check if a string is a palindrome.
def palindrom(string):
    return string==string[::-1]
string="civic"
print(palindrom(string))

print("_______________")

# 12 Create a function that takes a list of strings and returns a new list with the strings sorted alphabetically.
def sort_list(list):
    return sorted(list)
list=['banana','cherry','apple']
print(sort_list(list))

print("_______________")

# 13 Write a function to calculate the square of a number.
def square_num(number):
    return number**2
number=4
print(square_num(number))

print("_______________")

# 14 Create a function that takes two lists and returns True if they have at least one common element, otherwise False.
def common_element(list1,list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
               return True
        return False
list1=['apple','banana','cherry']
list2=['mango','apple',]
print(common_element(list1,list2))

print("_______________")

# 15 Write a function to calculate the power of a number.
def power(base,exponent):
    return  base * exponent
base=2
exponent=3
print(power(base,exponent))

print("_______________")

# 16 Write a function to merge two dictionaries.

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dictionaries(dict1, dict2))

print("_______________")
























































































































































