Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(1.01 - .99)
0.020000000000000018
>>> 2+6
8
>>> result=
SyntaxError: invalid syntax
>>> result=_
>>> result
8
>>> _
8
>>> "Christy" * 2
'ChristyChristy'
>>> "Otoboh!" *3
'Otoboh!Otoboh!Otoboh!'
>>> '4'*6
'444444'
>>> int(3.9)
3
>>> float(7)
7.0
>>> 12/4
3.0
>>> 12//4
3
>>> #use the // to get an interger division as the division will give float
>>> #modulo calculates the remainder of a division operation %
>>> 5%4
1
>>> 1hjf
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> #power is given by **
>>> 4**2
16
>>> #operator module provides function for common maths operations
>>> import operator
>>> operator.add(30,60)
90
>>> #Exercise
>>> 
>>> hours=(6.2,7,8,5,6.5,7.1,8.5)
>>> import operator
>>> operator.average(hours)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    operator.average(hours)
AttributeError: module 'operator' has no attribute 'average'
>>> operator.add(hours)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    operator.add(hours)
TypeError: add expected 2 arguments, got 1
>>> hours=(6.2+7+8+5+6.5+7.1+8.5)
>>> hours
48.300000000000004
>>> ave_hours=hours/6
>>> ave_hours
8.05
>>> 297%3
0
>>> 297/3
99.0
>>> 99*3
297
>>> 2**10
1024
>>> leap=(1800,1900,1903,2000,2002)%4
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    leap=(1800,1900,1903,2000,2002)%4
TypeError: unsupported operand type(s) for %: 'tuple' and 'int'
>>> 1800%4
0
>>> 1900%4
0
>>> 1903%4
3
>>> 2000%4
0
>>> 2002%4
2
>>> (1800 1900 1903 2000 2002)%4
SyntaxError: invalid syntax
>>> 1800%4%100
0
>>> 1800%100
0
>>> 1900%4%100
0
>>> 1903%4%100
3
>>> 1903%100
3
>>> 1903%4%100%400
3
>>> 1903%400
303
>>> 