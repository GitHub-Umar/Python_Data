                                            #[ Sets in PYthon ]

#[ Sets ]
a={'apple','banana','mango'}
b={1,2,3,4,5}
print(a)
print(b)

print("_______________")

#[ Dublicate values are not allower in set ]
a={'apple','banana','mango','apple'}
print(a)

print("_______________")

#[ Set items can be of any data type ]
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

print("_______________")

#[ Add Items in a  set ]
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "mango", "papaya"}
set1.update(set2)
print(set1)

print("_______________")

#[ Remove Item in a  set ]
set = {"apple", "banana", "cherry"}
set.remove('cherry')
print(set)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

set = {"apple", "banana", "cherry"}
x=set.pop()
print(x)
print(set)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

print("_______________")

#[ Join Sets ]
'''
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''
#[ Union ]
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

print("_______________")

#[ Intersection keep only the dublicats & ]
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

print("_______________")

#[ Difference Keep all items from set1 that are not in set2 ]
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

print("_______________")

#[ Symmetric Differences Keep the items that are not present in both sets ]
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

print("_______________")

#[ isdisjoint method Return True if no items in set x is present in set y ]
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)

print("_______________")

#[ issubset method Return True if all items in set x are present in set y ]
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x<=y
print(z)

print("_______________")

#[ issuperset() Method  Return True if all items set y are present in set x ]
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c","z"}
z = x>=y
print(z)






