Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#Arithematic Operator

a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16

#Assignment Operator

a=2
b=5

print(a+=b)
SyntaxError: invalid syntax
a+=b
a
7
a-=b
a
2
a/=b
a
0.4
a//=b
a
0.0
a**=b
a
0.0
a*=b
a
0.0
a%=b
a
0.0
b+=a
b
5.0

#Comparison Operator

a=6
b=9
a<b
True
a>b
False
a<=b
True
a>=b
False
a!=b
True
a==b
False

#Logical Operator

a=10
b=20

a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
True
True
not False
True

#Identity Operator
a=3
type
<class 'type'>
type(a) is int
True
type(a) is not int
False
type(a) is not float
True
>>> a=5.6
>>> type(a) is float
True
>>> type(a) is not int
True
>>> type(a) is not float
False
>>> type(a) is str
False
>>> type(a) is not str
True
>>> type(a) is not bool
True
>>> type(a) is bool
False
>>> type(a) is complex
False
>>> type(a) is not complex
True
>>> 
>>> #Membership Operator
>>> 
>>> a=2,3,4,5,6,7,8,9,10
>>> 9 in a
True
>>> 20 not in a
True
>>> 20 in a
False
3 in a
True
3 not in a
False

#Bitwise Operator

a=3
b=6
a&b
2
bin(2)
'0b10'
bin(3)
'0b11'
bin(6)
'0b110'

a=3
b=6
a&b
2
bin(3)
'0b11'
bin(6)
'0b110'
a=2
b=4
a|b
6
a=5
b=7
a|b
7

#Negotiation Formula

a=5
-(a+1)
-6
~a
-6
a=-7
~a
6
-(a+1)
6

a=3
b=5
a^b
6
a=4
a<<2
16
bin(4)
'0b100'
a=8
a<<3
64
a=9
a>>3
1
