Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Completion of strings exercise question 4 answer.
>>> 
>>> item="car"
>>> cost=13499.99
>>> print(item:"{:<10.2f,}".format(cost))
SyntaxError: invalid syntax
>>> print(item:{:<10.2f,}.format(cost))
SyntaxError: invalid syntax
>>> print('item:{:<10.2f,}'.format(cost))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('item:{:<10.2f,}'.format(cost))
ValueError: Invalid format specifier
>>> print('{:<10} {:>10.2f}.format(item, cost))
      
SyntaxError: EOL while scanning string literal
>>> print('{:<10} {:>10.2f}'.format(item, cost))
car          13499.99
>>> print('{:<10} {:>,10.2f}.format(item, cost))
      
SyntaxError: EOL while scanning string literal
>>> print('{:<10} {:>,10.2f}'.format(item, cost))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print('{:<10} {:>,10.2f}'.format(item, cost))
ValueError: Invalid format specifier
>>>  print('{:<10} {:>,10.2f,}'.format(item, cost))
 
SyntaxError: unexpected indent
>>> SyntaxError: unexpected indent
SyntaxError: invalid syntax
>>> print('{:<10} {:>,10.2f,}'.format(item, cost))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print('{:<10} {:>,10.2f,}'.format(item, cost))
ValueError: Invalid format specifier
>>> print('{:<10} {:>10.2f,}'.format(item, cost))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print('{:<10} {:>10.2f,}'.format(item, cost))
ValueError: Invalid format specifier
>>> print('{:<10} {:>10.2f,}'.format(item, cost))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print('{:<10} {:>10.2f,}'.format(item, cost))
ValueError: Invalid format specifier
>>> print('{:<10} {:,>10.2f}'.format(item, cost))
car        ,,13499.99
>>> print('{:<10} {:>10.2,f}'.format(item, cost))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print('{:<10} {:>10.2,f}'.format(item, cost))
ValueError: Invalid format specifier
>>> print('{:<10} {:>10,.2f}'.format(item, cost))
car         13,499.99
>>> #finall answer found above
>>> 
>>> 
>>> 