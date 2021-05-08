Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'bar'.startswith(b)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    'bar'.startswith(b)
NameError: name 'b' is not defined
>>> 'bar'.startswith('b')
True
>>> #Boolean is a built in function that represents TRUE or FALSE Values as shown above.
>>> a=True
>>> b=False
>>> type(a)
<class 'bool'>
>>> a==True
True
>>> bool(a)
True
>>> ('')
''
>>> print('')

>>> a=()
>>> print(a)
()
>>> bool('')
False
>>> #Empty Strings behave falsy as shown above while it behaves truthy if any character is passed to them.
>>> name='Paul'
>>>  if name:
	 
SyntaxError: unexpected indent
>>> name=input('Please insert name here:')
>>> print(name)
Please insert name here:Paul
>>> print(name)
Paul
>>> name=input('Please insert name here:')
Please insert name here:
>>> name='Paul'
>>> if name:
	print('The name is {}'.format(name))
	else:
		
SyntaxError: invalid syntax
>>> if name:
	print('The name is {}'.format(name))
	else:\n
	
SyntaxError: invalid syntax
>>> if name:
	print('The name is {}'.format(name))
	else: print('The name is missing')
	
SyntaxError: invalid syntax
>>> name=input('Please insert name here:')
Please insert name here:Paul
>>> if name:
	print('The name is {}'.format(name))
	else: print('The name is missing')
	
SyntaxError: invalid syntax
>>> >>> name=input('Please insert name here:')
Please insert name here:Paul
>>> if name:
	print('The name is {}'.format(name))

	
SyntaxError: invalid syntax
>>> 
>>> 
>>> ##Values that are considered false in python are None, False, Zero of any numeric type, empty sequence, empty mapping,object of classes which has _bool_(), _len_().   All other values return TRUE.
>>> 
>>> test[]
SyntaxError: invalid syntax
>>> test=[]
>>> print(test, 'is',bool(test))
[] is False
>>> test=([],[0],0.0,None,True,"easy string")
>>> print(test, 'is',bool(test))
>>> print(test, 'is',bool(test))
([], [0], 0.0, None, True, 'easy string') is True
>>> test=[]
>>> print(test, 'is',bool(test))
SyntaxError: multiple statements found while compiling a single statement
>>> exam=[]
>>> print(exam,'is' bool(exam))
SyntaxError: invalid syntax
>>> print(exam,'is',bool(exam))
[] is False
>>>  exam=[0]
>>> print(exam,'is', bool(exam))
SyntaxError: unexpected indent
>>> exam=[0]
>>> print(exam,'is', bool(exam))
SyntaxError: multiple statements found while compiling a single statement
>>> exam=[0]
>>> print(exam,'is', bool(exam))
SyntaxError: multiple statements found while compiling a single statement
>>> exam=[0]
>>> print(exam,'is', bool(exam))
[0] is True
>>> exam=None
>>> print(exam,'is', bool(exam))
SyntaxError: multiple statements found while compiling a single statement
>>> exam=None
>>> print(exam, 'is',bool(exam))
None is False
>>> True+(False/True)
1.0
>>> True==0
False
>>> False==1
False
>>> done='a'
>>> print(done,'is', bool(done))
a is True
>>> if done:
	print("a is true indeed")

	
a is true indeed
>>> else done:
	
SyntaxError: invalid syntax
>>> if else:
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> if done:
	print("ok!')
	      
SyntaxError: EOL while scanning string literal
>>> if done:
	print("ok!")
	else:
		
SyntaxError: invalid syntax
>>> if done:
	print("ok!")
	
	else:
		
SyntaxError: invalid syntax
>>> if done:
	print("ok!")
else:
	print("not Ok!")

	
ok!
>>> name='Christy'
>>> if name:
	print("The name is {}".format(name))
else:
	print("The name is missing!")

	
The name is Christy
>>> name=input("insert name here:")
insert name here:
>>> if name:
	print("The name is {}".format(name))
else:
	print("The name is missing!")

The name is missing!
>>> members=[]
>>> if members:
	print("members have values {}".format(members))
else:
	print("empty list")

	
empty list
>>>  members=["Olu","Bimbo"]
>>> if members:
	print("members have values {}".format(members))
else:
	print("empty list")
	
SyntaxError: unexpected indent
>>> members=["Bimbo","Olu"]
>>> if members:
	print("members have values {}".format(members))
else:
	print("empty list")
	
>>> 
>>>  members=["Bimbo","Olu"]
>>> if members:
	print("members have values {}".format(members))
else:
	print("empty list")
	
SyntaxError: unexpected indent
>>> members=["Bimbo","Olu"]
>>> if members:
	print("members have values {}".format(members))
else:
	print("empty list")
	
>>> class Nope:
	def _ _bool_ _(self):
		
SyntaxError: invalid syntax
>>> class Nope:
def _ _bool_ _(self):
	
SyntaxError: expected an indented block
>>> class Nope:
 def _ _bool_ _(self):
	 
SyntaxError: invalid syntax
>>>  class Nope:
	def __bool__(self):
		
SyntaxError: unexpected indent
>>> class Nope:
	def __bool__(self):
		return false

	
>>> n=Nope()
>>> bool(n)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    bool(n)
  File "<pyshell#95>", line 3, in __bool__
    return false
NameError: name 'false' is not defined
>>> class Nope:
	def __bool__(self):
		return false

	
>>> class Nope:
	def __bool__(self):
		return False

	
>>>  n=Nope()
>>> bool(n)
SyntaxError: unexpected indent
>>> n=Nope()
>>> bool(n)
SyntaxError: multiple statements found while compiling a single statement
>>> n=Nope()
>>> bool(n)
False
>>> age=27
>>> old=18
>>> old=18
>>> age=27
>>> old=(age>18)
>>> print(old)
True
>>> names=["Bukola", "Olu", "China"]
>>> if names:
	print("Class has enrollments {}".format(names))
else:
	print("This class is empty!")

	
Class has enrollments ['Bukola', 'Olu', 'China']
>>>  names=[]
>>> if names:
	print("Class has enrollments {}".format(names))
else:
	print("This class is empty!")

SyntaxError: unexpected indent
>>> names=[]
>>> if names:
	print("Class has enrollments {}".format(names))
else:
	print("This class is empty!")

SyntaxError: multiple statements found while compiling a single statement
>>> names=[]
>>> if names:
	print("Class has enrollments {}".format(names))
else:
	print("This class is empty!")

	
This class is empty!
>>> car=None
>>> if None:
	print("Taxi for you")
else:
	print("you have a car!")

	
you have a car!
>>> print(car)
None
>>> car(Toyota)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    car(Toyota)
NameError: name 'Toyota' is not defined
>>> car(None=Toyota)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> car(None=="Toyota")
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    car(None=="Toyota")
TypeError: 'NoneType' object is not callable
>>>  car(None==Toyota)
 
SyntaxError: unexpected indent
>>> car(None==Toyota)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    car(None==Toyota)
NameError: name 'Toyota' is not defined
>>> 