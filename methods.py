Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name="damilola"
>>> print(name)
damilola
>>> correct="name".capitalize()
>>> correct
'Name'
>>> correct=name.capitalize()
>>> correct
'Damilola'
>>> print(name)
damilola
>>> #in passing a method with a string, a new string s created just as shown above because strings are immutable.
>>> last='fatile'
>>> last
'fatile'
>>> print('fatile'.capitalize())
Fatile
>>> #Everything in python is an object hence intergers and floats also have methods passed to them.
>>> 4
4
>>> dir(4)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> print(4.numerator)
SyntaxError: invalid syntax
>>> print(4.float)
SyntaxError: invalid syntax
>>> print(4.float())
SyntaxError: invalid syntax
>>> print(4.numerator())
SyntaxError: invalid syntax
>>> 4.conjugate()
SyntaxError: invalid syntax
>>> 5.conjugate()
SyntaxError: invalid syntax
>>> (4).float()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    (4).float()
AttributeError: 'int' object has no attribute 'float'
>>> (4).numerator()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    (4).numerator()
TypeError: 'int' object is not callable
>>> (4).conjugate()
4
>>> #inorder ro invoke a method on a float/integer, wrap the number with () or assign a variable to the interger and then call the mthod on the variable.
>>> four=4
>>> four.conjugate()
4
>>> cs='Oct3482.csv'
>>> cs.endswith('.csv')
True
>>> cs.endswith('.xls')
False
>>> cs.startswith()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    cs.startswith()
TypeError: startswith() takes at least 1 argument (0 given)
>>> cs.startswith('Oct')
True
>>> word='grateful'
>>> word
'grateful'
>>> word.find('ate')
2
>>> word.find('ful')
5
>>> word.startswith('gra')
True
>>> 