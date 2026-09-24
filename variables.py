Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(4+8)
12
a=10
print(a)
10
x=50
print(X)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
50
Z=100
print(Z)
100
a3=90
print(a3)
90
a0123456789=100
print(a123456789)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(a123456789)
NameError: name 'a123456789' is not defined. Did you mean: 'a0123456789'?
print(a0123456789)
100
name="manu"
print(name)
manu
print("name")
name
city="vja"
print(city)
vja
country="India"
print(country)
India
a=8
b=9
print(a+b)
17
fname="manu"
lname="dh"
print(fname+lname)
manudh
print(fname+" "+1name)
SyntaxError: invalid decimal literal
print(fname+" "+lname)
manu dh
a=3, b=7
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=9
print(a+b)
13
a,b=6,7
print(a+b)
13
a=4
b=8
print(a+b)
12
@=10
SyntaxError: invalid syntax
$=10
SyntaxError: invalid syntax
_=40
print(_)
40
_a=100
print(_a)
100
if=20
SyntaxError: invalid syntax
while=20
SyntaxError: invalid syntax
a=2,3,4,5,6,7,8,9
print(a)
(2, 3, 4, 5, 6, 7, 8, 9)
a,b,c=3,4,5
print(a,b,c)
3 4 5
a,b,c=4,5,6,7,8,9,10
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a,b,c=4,5,6,7,8,9,10
ValueError: too many values to unpack (expected 3, got 7)
first name="manu"
SyntaxError: invalid syntax
first_name="manu"
print(first_name)
manu
>>> firstname="manu"
>>> print(firstname)
manu
>>>  a=3
...  
SyntaxError: unexpected indent
>>> _a=9
>>> print(_a)
9
>>> a=(1,2,3)
>>> print(a)
(1, 2, 3)
>>> a,b,c=5,6,7
>>> print(a.b,c)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(a.b,c)
AttributeError: 'int' object has no attribute 'b'
>>> print(a,b,c)
5 6 7
>>> a=90
>>> print(a)
90
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a3'?
>>> name="manu"
>>> print(name)
manu
>>> Name="manu"
>>> print(Name)
manu
>>> NAME="manu)
SyntaxError: unterminated string literal (detected at line 1)
>>> NAME="manu"
>>> print(NAME)
manu
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print(a,b,c)
10 10 10
