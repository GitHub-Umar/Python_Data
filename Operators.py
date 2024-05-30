                              #[ Operators in Python ]
#[ Arithmetic operators ]
'''
+	Addition	   x + y                       
-	Subtraction	   x - y	
*	Multiplication x * y	
/	Division	   x / y	
%	Modulus	       x % y	
**	Exponentiation x ** y	
//	Floor division x // y
'''
x=3
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

print("_______________")

#[ Assignment operators ]
'''
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3
'''
x=2
x+=3
print(x)
x=2
x-=3
print(x)
x=2
x*=3
print(x)
x=2
x%=3
print(x)
x=2
x/=3
print(x)
x=2
x//=3
print(x)
x=2
x**=3
print(x)

print("_______________")

#[ Comparison Operators ]
'''
==	Equal	         x == y	
!=	Not equal	     x != y	
>	Greater than	 x > y	
<	Less than	     x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	    x <= y
'''

x=3
y=2
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

print("_______________")

#[ Logical Operators ]
'''
and Returns True if both statements are true	    x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	 not(x < 5 and x < 10)
'''
x=6
print(x>5 and x<10)
print(x>7 or x<10)
print(not(x < 5 and x < 10))

#[  Identity Operators ]
'''
in 	    Returns True if a sequence with the specified value is present in the object	
        x in y	
not in	Returns True if a sequence with the specified value is not present in the object
	    x not in y
'''

x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("cherry"not in x)
