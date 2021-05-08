Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name="Mmachi"
>>> print("Hello{}".format(name))
HelloMmachi
>>> print("Hello {}".format(name))
Hello Mmachi
>>> ##replacement field syntax for strings using .format
>>> "Name: {}".format("farrel")
'Name: farrel'
>>> 'Name: {name}'.format(name='Joy')
'Name: Joy'
>>> print("a:{}","b:{}","c:{}".format(2,3,4))
a:{} b:{} c:2
>>> print("a:{}","b:{}","c:{}".format(4),(2),(1))
a:{} b:{} c:4 2 1
>>> print("a:,b:,c:{}".format(2,3,4))
a:,b:,c:2
>>> print("a:{},b:{},c:{}".format(2,3,4))
a:2,b:3,c:4
>>> print('d:{},e:{},f:{}".format(pen,classic,rugged))
      
SyntaxError: EOL while scanning string literal
>>>  print('d:{},e:{},f:{}'.format(pen,classic,rugged))
 
SyntaxError: unexpected indent
>>> print('d:{},e:{},f:{}'.format(pen,classic,rugged))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print('d:{},e:{},f:{}'.format(pen,classic,rugged))
NameError: name 'pen' is not defined
>>> print('d:{},e:{},f:{}'.format("pen","classic","rugged"))
d:pen,e:classic,f:rugged
>>>  print('d={},e={},f={}'.format(pen,classic,rugged))
 
SyntaxError: unexpected indent
>>> print('d={},e={},f={}'.format("pen","classic","rugged"))
d=pen,e=classic,f=rugged
>>> 'name:{}'.format("Paul)
		 
SyntaxError: EOL while scanning string literal
>>> 'name:{}'.format("Paul")
'name:Paul'
>>> 'name:{name}'.format(name="John")
'name:John'
>>> 'name:{[name]}'.format{("George"})
SyntaxError: invalid syntax
>>> 'name:{[name]}'.format({"George"})
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    'name:{[name]}'.format({"George"})
TypeError: 'set' object is not subscriptable
>>> 'name:{[name]}'.format({'name':'George'})
'name:George'
>>> 'Last:{2}First:{0}'.format('Paul', 'John',
			   'George')
'Last:GeorgeFirst:Paul'
>>> 'Last: {2}First: {0}'.format('Paul', 'John',
			   'George')
'Last: GeorgeFirst: Paul'
>>> 'Last: {2} First: {0}'.format('Paul', 'John',
			   'George')
'Last: George First: Paul'
>>> 'Last: {2} First: {1}'.format('Paul', 'John',
			   'George')
'Last: George First: John'
>>> 'now:{>}'.format('Christy')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    'now:{>}'.format('Christy')
KeyError: '>'
>>> 'car:{[.precision]}'.format([89/2])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    'car:{[.precision]}'.format([89/2])
TypeError: list indices must be integers or slices, not str
>>> car:{[.precision]}.format([89/2])
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> 'car:{[.precision]}'.format(89/2)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    'car:{[.precision]}'.format(89/2)
TypeError: 'float' object is not subscriptable
>>> 'car:{.precision}'.format(89/2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    'car:{.precision}'.format(89/2)
AttributeError: 'float' object has no attribute 'precision'
>>> 'rin:{:*^12}'.format("Ringo)
		     
SyntaxError: EOL while scanning string literal
>>> 'rin:{:*^12}'.format("Ringo")
'rin:***Ringo****'
>>> 'coo:{:$<10}'.format('Christiana')
'coo:Christiana'
>>> 'rin:{:*<12}'.format("Ringo")
'rin:Ringo*******'
>>> 'rin:{:+^12}'.format("Ringo")
'rin:+++Ringo++++'
>>> 'rin:{:$^12}'.format("Ringo")
'rin:$$$Ringo$$$$'
>>> 'rin:{:*^10}'.format("Ringo")
'rin:**Ringo***'
>>> 'rin:{:$<10}'.format("Ringo")
'rin:Ringo$$$$$'
>>> 'rin:{:*^12}'.format("Christina")
'rin:*Christina**'
>>> 'rin:{:*^10}'.format("Christina")
'rin:Christina*'
>>> 'rin:{:^12}'.format("Ringo")
'rin:   Ringo    '
>>> 'rin:{:>12}'.format("Ringo")
'rin:       Ringo'
>>> 
>>> "percent:{:=+10.1%}".format(44/100)
'percent:+    44.0%'
>>> "percent:{:=+10.1%}".format(-44/100)
'percent:-    44.0%'
>>> "percent:{:=+10.5%}".format(44/100)
'percent:+44.00000%'
>>> "percent:{:=+20.1%}".format(44/100)
'percent:+              44.0%'
>>> "percent:{:=+5.1%}".format(44/100)
'percent:+44.0%'
>>> "percent:{:=+5.5%}".format(-44/100)
'percent:-44.00000%'
>>> "percent:{:=+1.1%}".format(100/100)
'percent:+100.0%'
>>> 'anoth:{:=+}'.format(20/100)
'anoth:+0.2'
>>> 'anoth:{:=+%}'.format(20/100)
'anoth:+20.000000%'
>>> 'anoth:{:=+4.2%}'.format(20/100)
'anoth:+20.00%'
>>> 'anoth:{:=+10.2%}'.format(20/100)
'anoth:+   20.00%'
>>> 'anoth:{:=+4.2%}'.format(-20/100)
'anoth:-20.00%'
>>> 'anoth:{:=+4,}'.format(2000000)
'anoth:+2,000,000'
>>> 'anoth:{:=+20_}'.format(-1000000)
'anoth:-          1_000_000'
>>> 'anoth:{:-=+20_}'.format(-1000000)
'anoth:-----------1_000_000'
>>> 'anoth:-----------1_000_000'
'anoth:-----------1_000_000'
>>> 'anoth:{:=+50b}'.format(1000000)
'anoth:+                             11110100001001000000'
>>>  'anoth:{:=+10b}'.format(1000000)
 
SyntaxError: unexpected indent
>>> 'anoth:{:=+10b}'.format(1000000)
'anoth:+11110100001001000000'
>>> 'Binary:{:+b}'.format(12)
'Binary:+1100'
>>> "Hex:{:*5>X}".format(21)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    "Hex:{:*5>X}".format(21)
ValueError: Invalid format specifier
>>> "Hex:{:*>X}".format(21)
'Hex:15'
>>> "Hex:{:*>5X}".format(21)
'Hex:***15'
>>> "Hex:{:x}".format(21)
'Hex:15'
>>> "Hex:{:x}".format(12)
'Hex:c'
>>> name="Miracle"
>>> f'My name is {name}'
'My name is Miracle'
>>> new="chris"
>>> f"My name is {name.uppercase()}
SyntaxError: EOL while scanning string literal
>>> f"My name is {name.uppercase()}"
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    f"My name is {name.uppercase()}"
AttributeError: 'str' object has no attribute 'uppercase'
>>>  f"My name is {name.capitalize()}"
 
SyntaxError: unexpected indent
>>> f"My name is {name.capitalize()}
SyntaxError: EOL while scanning string literal
>>> 
KeyboardInterrupt
>>> f"My name is {name.capitalize()}"
'My name is Miracle'
>>> f"My name is {new.capitalize()}
SyntaxError: EOL while scanning string literal
>>> f"My name is {new.capitalize()}"
'My name is Chris'
>>> nom=12345
>>> f'{nom.string}
SyntaxError: EOL while scanning string literal
>>> f'{nom.string}'
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    f'{nom.string}'
AttributeError: 'int' object has no attribute 'string'
>>> f'multplication of these two numbers are: {8*8}'
'multplication of these two numbers are: 64'
>>> #Exercise
>>> 
>>> name="Christiana Otoboh"
>>> age=27
>>> print(name is age)
False
>>> 'name is{}'.format(age)
'name is27'
>>> print(name, 'is{}'.format(age))
Christiana Otoboh is27
>>> print(name, 'is{} '.format(age))
Christiana Otoboh is27 
>>> print(name, 'is{}' .format(age))
Christiana Otoboh is27
>>> print(name, 'is{} '.format(age))
Christiana Otoboh is27 
>>> print(name, 'is{}' .format(age))
Christiana Otoboh is27
>>> print(name, 'is {}'.format(age))
Christiana Otoboh is 27
>>> print(name, 'is {}'.format(age),"years old.")
Christiana Otoboh is 27 years old.
>>> paragraph='''\"Python is a great language!",said Fred.\"I don't ever remeber\n
having this much fun before".'''
>>> print(paragraph)
"Python is a great language!",said Fred."I don't ever remeber

having this much fun before".
>>> '''\"Python is a great language!",said Fred.\"I don't ever remeber\n
having this much fun before".'''
>>> print(paragraph)
'"Python is a great language!",said Fred."I don\'t ever remeber\n\nhaving this much fun before".'
>>> paragraph='''\"Python is a great language!",said Fred.\"I don't ever remeber\t
having this much fun before".'''
>>> print(paragraph)
"Python is a great language!",said Fred."I don't ever remeber	
having this much fun before".
>>> paragraph='''\"Python is a great language!",said Fred. \"I don't ever remeber\n
having this much fun before".'''
>>> print(paragraph)
"Python is a great language!",said Fred. "I don't ever remeber

having this much fun before".
>>> paragraph='''\"Python is a great language!",said Fred. \"I don't ever remeber\t
having this much fun before".'''
>>> print(paragraph)
"Python is a great language!",said Fred. "I don't ever remeber	
having this much fun before".
>>> paragraph='''\"Python is a great language!",said Fred.\"I don't ever remeber\t
having this much fun before."'''
>>> print(paragraph)
"Python is a great language!",said Fred."I don't ever remeber	
having this much fun before."
>>> omega='\03A9'
>>> print(omega)
A9
>>> omega='\03A9','\GREEK CAPITAL LETTER OMEGA'
>>> omega
('\x03A9', '\\GREEK CAPITAL LETTER OMEGA')
>>>  omega='\03A9{GREEK CAPITAL LETTER OMEGA}'
 
SyntaxError: unexpected indent
>>> omega='\03A9{GREEK CAPITAL LETTER OMEGA}'
>>> print(omega)
A9{GREEK CAPITAL LETTER OMEGA}
>>> omega=('\u03A9','\N{GREEK CAPITAL LETTER OMEGA}')
>>> print(omega)
('Ω', 'Ω')
>>> omeg=('\u03A9')
>>> omeg
'Ω'
>>> than=('\0384')
>>> than
'\x0384'
>>> than=('\u0384')
>>> than
'΄'
>>> rho=('\u03A1)
     
SyntaxError: EOL while scanning string literal
>>> rho=('\u03A1')
>>> rho
'Ρ'
>>> item='car
SyntaxError: EOL while scanning string literal
>>> item='car'
>>> cost=13499.99
>>> print('{<10}'.format(item),'{>10.2,}'.format(cost))
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    print('{<10}'.format(item),'{>10.2,}'.format(cost))
KeyError: '<10'
>>> print('{<10},{>10.2,}'.format(cost,item))
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    print('{<10},{>10.2,}'.format(cost,item))
KeyError: '<10'
>>> print('{<10}{>10.2,}'.format(cost,item))
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    print('{<10}{>10.2,}'.format(cost,item))
KeyError: '<10'
>>> print('{ <10}{>10.2,}'.format(cost,item))
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    print('{ <10}{>10.2,}'.format(cost,item))
KeyError: ' <10'
>>> print('{ <10}{>10.2,}'.format(item,cost))
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    print('{ <10}{>10.2,}'.format(item,cost))
KeyError: ' <10'
>>> '{>10.2,}'.format(cost)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    '{>10.2,}'.format(cost)
KeyError: '>10'
>>> print('item:{:<10} cost:{>10.2,}'.format(item,cost))
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    print('item:{:<10} cost:{>10.2,}'.format(item,cost))
KeyError: '>10'
>>> print('{:<10} {>10.2,}'.format(item,cost))
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    print('{:<10} {>10.2,}'.format(item,cost))
KeyError: '>10'
>>> print('{:<10} {:>10.2,}'.format(item,cost))
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    print('{:<10} {:>10.2,}'.format(item,cost))
ValueError: Unknown format code ',' for object of type 'float'
>>>  print('{:<10} {:>10.2 ,}'.format(item,cost))
 
SyntaxError: unexpected indent
>>> print('{:<10} {:>10.2 ,}'.format(item,cost))
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    print('{:<10} {:>10.2 ,}'.format(item,cost))
ValueError: Invalid format specifier
>>> 
KeyboardInterrupt
>>> cost=1349999
>>> print('{:<10} {:>10.2,}'.format(item,cost))
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    print('{:<10} {:>10.2,}'.format(item,cost))
ValueError: Unknown format code ',' for object of type 'int'
>>> cost=13499.99
>>> print('{:<10} {:>10.2,}'.format(item,cost))
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    print('{:<10} {:>10.2,}'.format(item,cost))
ValueError: Unknown format code ',' for object of type 'float'
>>> '{:<10,>10.2,}'.format(item,cost)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    '{:<10,>10.2,}'.format(item,cost)
ValueError: Invalid format specifier
>>> '{: <10}, {: >10.2,}',format(item,cost)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    '{: <10}, {: >10.2,}',format(item,cost)
TypeError: format() argument 2 must be str, not float
>>> '{: <10}, {: >10.2,}',format(item,'cost')
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    '{: <10}, {: >10.2,}',format(item,'cost')
ValueError: Invalid format specifier
>>>  '{: <10}, {: >10.2,}'.format(item,cost)
 
SyntaxError: unexpected indent
>>> 
'{: <10}, {: >10.2,}'.format(item,cost)
Traceback (most recent call last):
  File "<pyshell#151>", line 2, in <module>
    '{: <10}, {: >10.2,}'.format(item,cost)
ValueError: Unknown format code ',' for object of type 'float'
>>> '{: <10}, {: >10.2,}'.format(item, 'cost')
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    '{: <10}, {: >10.2,}'.format(item, 'cost')
ValueError: Unknown format code ',' for object of type 'str'
>>> 'item:{: <10}, cost:{: >10.2,}'.format("car", 13499.99)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    'item:{: <10}, cost:{: >10.2,}'.format("car", 13499.99)
ValueError: Unknown format code ',' for object of type 'float'
>>> 'item:{: <10}, cost:{: >.2,}'.format("car", 13499.99)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    'item:{: <10}, cost:{: >.2,}'.format("car", 13499.99)
ValueError: Unknown format code ',' for object of type 'float'
>>> "percent:{:=+10.1}".format(13.24)
'percent:+    1e+01'
>>> "percent:{:>3.2}".format(13.24)
'percent:1.3e+01'
>>> "percent:{:>3.2}".format(13.24)
'percent:1.3e+01'
>>> 'cost:{:>10.2}'.format(13499.99)
'cost:   1.3e+04'
>>> 'cost:{:>10.2,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    'cost:{:>10.2,}'.format(13499.99)
ValueError: Unknown format code ',' for object of type 'float'
>>> 
KeyboardInterrupt
>>> 'cost:{:>,10.2}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    'cost:{:>,10.2}'.format(13499.99)
ValueError: Invalid format specifier
>>> 'cost:{:,>10.2}'.format(13499.99)
'cost:,,,1.3e+04'
>>> 'cost:{:,<10.2}'.format(13499.99)
'cost:1.3e+04,,,'
>>> 'cost:{:<10.2,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    'cost:{:<10.2,}'.format(13499.99)
ValueError: Unknown format code ',' for object of type 'float'
>>> 'cost:{:=<10.2,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    'cost:{:=<10.2,}'.format(13499.99)
ValueError: Unknown format code ',' for object of type 'float'
>>> 'cost:{:<.2,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    'cost:{:<.2,}'.format(13499.99)
ValueError: Unknown format code ',' for object of type 'float'
>>> 'cost:{:<10.,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    'cost:{:<10.,}'.format(13499.99)
ValueError: Format specifier missing precision
>>> 'cost:{:<10.2 ,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    'cost:{:<10.2 ,}'.format(13499.99)
ValueError: Invalid format specifier
>>> 'cost:{:<10.2f,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    'cost:{:<10.2f,}'.format(13499.99)
ValueError: Invalid format specifier
>>> 'cost:{:<10.2g,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    'cost:{:<10.2g,}'.format(13499.99)
ValueError: Invalid format specifier
>>> 'cost:{:<10.g,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    'cost:{:<10.g,}'.format(13499.99)
ValueError: Format specifier missing precision
>>> 'cost:{:n<10.,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    'cost:{:n<10.,}'.format(13499.99)
ValueError: Format specifier missing precision
>>> 'cost:{:n<10.2,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    'cost:{:n<10.2,}'.format(13499.99)
ValueError: Unknown format code ',' for object of type 'float'
>>> 'cost:{:n<10.2}'.format(13499.99)
'cost:1.3e+04nnn'
>>> 'cost:{:<10.2}'.format(13499.99)
'cost:1.3e+04   '
>>> 'cost:{:+<10.2,}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    'cost:{:+<10.2,}'.format(13499.99)
ValueError: Unknown format code ',' for object of type 'float'
>>> 'cost:{:+<10.2}'.format(13499.99)
'cost:1.3e+04+++'
>>> 'cost:{:=+<10.2}'.format(13499.99)
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    'cost:{:=+<10.2}'.format(13499.99)
ValueError: Invalid format specifier
>>> 
    'cost:{:<10.2}'.format(13499.99)
    
SyntaxError: unexpected indent
>>> 'cost:{:<10.2}'.format(13499.99)
'cost:1.3e+04   '
>>> 