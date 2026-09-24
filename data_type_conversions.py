Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#data_type_conversions

#int
int(8)
8
int(6.7)
6
int("hi")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(8+9j)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int(8+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#float
float(2)
2.0
float(9.7)
9.7
float("manu")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float("manu")
ValueError: could not convert string to float: 'manu'
float(6+9j)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0

#str

>>> str(2)
'2'
>>> str(9.7)
'9.7'
>>> str("hello")
'hello'
>>> str(8+7i)
SyntaxError: invalid decimal literal
>>> str(8+7j)
'(8+7j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> #complex
>>> complex(5)
(5+0j)
>>> complex(7.8)
(7.8+0j)
>>> complex("hello")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex("hello")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> #bool
>>> bool(7)
True
>>> bool(9.8)
True
>>> bool("hello")
True
>>> bool(8+9j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> 
>>> #In int string and complex cannot be converted
>>> #In float string and complex cannot be converted
>>> #In string all datatypes can be converted as python is a string based language
>>> #In complex string cannot be converted
>>> #In boolean all datatypes can be coverted as it is only True or False
