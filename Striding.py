Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> #Positive Striding
>>> a="Machine Learning"
>>> a[::4]
'MiLn'
>>> a[::6]
'Men'
>>> a[5:]
'ne Learning'
>>> a[:9]
'Machine L'
>>> a[::7]
'M n'
>>> 
>>> a="Cloud Computing"
>>> a[2:14:4]
'oCu'
>>> a[5:13:3]
' mt'
>>> a[4:12:2]
'dCmu'
>>> 
>>> #Negative Striding
>>> a="Python Course"
>>> a[-7:-11:-2]
' o'
a[-1:-11:-2]
'ero o'
a[-2:-12:-3]
'sont'

a="Artificial Intelligence"
a[-11:-2:-4]
''
a[-5:-11:-2]
'gle'
a[-2:-10:-5]
'cl'
