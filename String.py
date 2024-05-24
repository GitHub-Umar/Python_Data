                                          #[ Strings in Python ]

#[ Assigning astring to a variable ]
a='apple'
print(a)

print("_______________")

#[ String are written in multiline or singleline quotes ]
a="umar"
b='Javed'
print(a,b)

print("_______________")

#[ use quotes inside a string, as long as they don't match the quotes surrounding the string ]
print("My name is 'Umar'")
print('My name is "Umar"')

print("_______________")

#[ Multiline sting use 3 double or single quotes]
a='''My name is Umar,
I am from Haroonabad.'''
print(a)

print("_______________")

#[ String are Arrays: Get character position and String Slicing ]
a='UmarJaved'
print(a[4])
print(a[0:])
print(a[:4])
print(a[4:9])
print(a[3:-1])
print(a[-5:-2])

print("_______________")

#[ Looping Through a String ]
for x in 'umar':
    print(x)

for y in ["apple","banana",'cherry']:
    print(y)

print("_______________")

#[ String Length ]
a="umarjaved"
print(len(a))

print("_______________")

#[ Check String ]
a="umarjaved"
print("javed" in a)

a="umarjaved"
print("jutt" in a)

a="umarjavd"
if 'umar' in a:
    print("yes")

a="umarjavd"
if 'jutt' not in a:
    print("No")

print("_______________")

#[ Modify String to upper/lower case ]
a='UmaR'
print(a.upper())
print(a.lower())

print("_______________")

#[ Remove Whitespace and Replace String and Split String ]
a=" umar javed "
print(a.strip())
print(a.replace('u','O'))
print(a.split())

print("_______________")

#[ String Concatenation Merge variable ]
a='umar'
b='javed'
c=a+" "+b
print(c)
print(a+b)

print("_______________")

#[ Format - Strings ]
name='umar'
intro=f"My name is {name}"
print(intro)

print("_______________")

#[ Placeholders and Modifiers ]
price=20
car=f'Car price is {price} lacs'
print(car)

price=20
car=f'Car price is {price:.2f} lacs'
print(car)

car=f'Car price is {2*10} lacs'
print(car)

print("_______________")

#[ Escape Characters..... ]

# \" Backslash double Quote
txt="python is a \"programming\" language"
print(txt)

# \'	Backslash Single Quote
txt = 'It\'s programming.'
print(txt)

# \\	double Backslash for add single backslash
txt = "This will insert one \\ (backslash)."
print(txt)

# \n	New Line
txt='My name is Umar\nI am from Haroonabad'
print(txt)

# \r	Carriage Return
txt="hallo\rworld"
print(txt)

# \t	Tab add 1 space
txt="hallo\tworld"
print(txt)

# \b	Backspace remove 1 space or character
txt="hallo\bworld"
print(txt)

# \f	Form Feed adding this  form feed
txt="hallo\fworld"
print(txt)

# \ooo	Octal value
txt="\110\145\154\154\157"
print(txt)

# \xhh	Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

print("_______________")

#[ String Methods ]
'''
capitalize()   Converts the first character to upper case
casefold() 	   Converts string into lower case
center()	   Returns a centered string
count()        Returns the number of times a specified value occurs in a string
encode()	   Returns an encoded version of the string
endswith()	   Returns true if the string ends with the specified value
expandtabs()   Sets the tab size of the string
find()	       Searches the string for a specified value and returns the position of where it was found
format()	   Formats specified values in a string
format_map()   Formats specified values in a string
index()	       Searches the string for a specified value and returns the position of where it was found
isalnum()	   Returns True if all characters in the string are alphanumeric
isalpha()	   Returns True if all characters in the string are in the alphabet
isascii()	   Returns True if all characters in the string are ascii characters
isdecimal()	   Returns True if all characters in the string are decimals
isdigit()	   Returns True if all characters in the string are digits
isidentifier() Returns True if the string is an identifier
islower()	   Returns True if all characters in the string are lower case
isnumeric()	   Returns True if all characters in the string are numeric
isprintable()  Returns True if all characters in the string are printable
isspace()	   Returns True if all characters in the string are whitespaces
istitle()	   Returns True if the string follows the rules of a title
isupper()	   Returns True if all characters in the string are upper case
join()	       Joins the elements of an iterable to the end of the string
ljust()	       Returns a left justified version of the string
lower()	       Converts a string into lower case
lstrip()	   Returns a left trim version of the string
maketrans()	   Returns a translation table to be used in translations
partition()	   Returns a tuple where the string is parted into three parts
replace()	   Returns a string where a specified value is replaced with a specified value
rfind()	       Searches the string for a specified value and returns the last position of where it was found
rindex()	   Searches the string for a specified value and returns the last position of where it was found
rjust()	       Returns a right justified version of the string
rpartition()   Returns a tuple where the string is parted into three parts
rsplit()	   Splits the string at the specified separator, and returns a list
rstrip()	   Returns a right trim version of the string
split()	       Splits the string at the specified separator, and returns a list
splitlines()   Splits the string at line breaks and returns a list
startswith()   Returns true if the string starts with the specified value
strip()	       Returns a trimmed version of the string
swapcase()	   Swaps cases, lower case becomes upper case and vice versa
title()	       Converts the first character of each word to upper case
translate()	   Returns a translated string
upper()	       Converts a string into upper case
zfill()	       Fills the string with a specified number of 0 values at the beginning
'''

#[ expandtabs()   Sets the tab size of the string ]
txt = "H\te\tl\tl\to"
print(txt.expandtabs(2))

#[ join()	       Joins the elements of an iterable to the end of the string ]
myTuple = ("John", "Peter", "Vicky")
print('@'.join(myTuple))

#[ ljust()	       Returns a left justified version of the string ]
txt = "banana"
x = txt.ljust(10)
print(x, "is my favorite fruit.")
txt='umar'
print(txt.ljust(10),"is my name.")

#[ maketrans()	   Returns a translation table to be used in translations ]
txt = "Hello Sam!"
mystr = str.maketrans("S", "j")
print(txt.translate(mystr))