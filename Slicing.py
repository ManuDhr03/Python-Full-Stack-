Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> #Positive Slicing
>>> a="Codegnan"
>>> a[0:4]
'Code'
>>> a[4:8]
'gnan'
>>> a[:4]
'Code'
>>> a[4:]
'gnan'
>>> 
>>> a="Work hard until you succeed"
>>> a[10:15]
'until'
>>> a[5:10]
'hard '
>>> a[0:5]
'Work '
>>> a[16:19]
'you'
>>> a[18:27]
'u succeed'
>>> [19:27]
SyntaxError: invalid syntax
a[19:27]
' succeed'

a="Time is very precious"
a[13:21]
'precious'
a[8:13]
'very '
a[0:5]
'Time '

a="I love Python"

#Negative Slicing
a="I love Python"
a[-11:-7]
'love'
a[-6:]
'Python'

a="Today is weekend"
a[-16:-11]
'Today'
a[-10:-8]
'is'
b[-7:]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    b[-7:]
NameError: name 'b' is not defined
a[-7:]
'weekend'
