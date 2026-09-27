Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> #Positive Indexing
>>> a="I am in class"
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a[2]+a[3]
'am'
>>> a[5]+a[6]
'in'
>>> a[1]
' '
>>> a[4]
' '
>>> a[7]
' '
>>> a="Vijayawada is a royal city"
>>> a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
>>> a[22]+a[23]+a[24]+a[25]
'city'
>>> a[11]+a[12]
'is'
>>> 
>>> #Negative Indexing
>>> a="Vizag is a city of destiny"
>>> a[-15]+a[-14]+a[-13]+a[-12]
'city'
a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'Vizag'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'

a="Simple is better than complex"
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'Simple'
