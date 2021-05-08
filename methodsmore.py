Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('name:{},age:{}'.\
      format("Mathew",46))
name:Mathew,age:46
>>> print("word".find("
		  
SyntaxError: EOL while scanning string literal
>>> print("word".find('
		  
SyntaxError: EOL while scanning string literal
>>> print("word".find("
		  
SyntaxError: EOL while scanning string literal
>>> print("word".\
      find('ord'))
1
>>> print('{} {} {} {} {}'.format(
	'hello'
	'to'
	'you'
	'and'
	'you'))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print('{} {} {} {} {}'.format(
IndexError: Replacement index 1 out of range for positional args tuple
>>> print('{} {} {} {} {}'.format(
	'hello',
	'to',
	'you',
	'and',
	'you',))
hello to you and you
>>> ','.join(['1','2','3'])
'1,2,3'
>>> '-'.join(['1','2','3'])
'1-2-3'
>>> '$'.join(['1','2','3'])
'1$2$3'
>>> '$'.join(['1', '2', '3'])
'1$2$3'
>>> print('$'.join(['1','2','3']))
1$2$3
>>> '   Hello Dear   '.strip()
'Hello Dear'
>>> '   Hello Dear   '.1strip()
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> '   Hello Dear   '.Istrip()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    '   Hello Dear   '.Istrip()
AttributeError: 'str' object has no attribute 'Istrip'
>>> '   Hello Dear   '.lstrip()
'Hello Dear   '
>>> '   Hello Dear   '.rstrip()
'   Hello Dear'
>>> input("Hello, what is your name?:".strip())
Hello, what is your name?:    CHristiana     Otoboh
'    CHristiana     Otoboh'
>>> hey=input("Hello, what is your name?:")
Hello, what is your name?: Christiana Otoboh
>>> print(hey.strip())
Christiana Otoboh
>>> hey=input("Hello, what is your name?:")
Hello, what is your name?:   Christiana  Otoboh
>>> print(hey.strip())
Christiana  Otoboh
>>> print(hey)
   Christiana  Otoboh
>>> print(hey.strip())
Christiana  Otoboh
>>> print(hey.lstrip())
Christiana  Otoboh
>>> school="Pilgrim Baptist school"
>>> dir(school)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(rsplit)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    help(rsplit)
NameError: name 'rsplit' is not defined
>>> help(school.rsplit)
Help on built-in function rsplit:

rsplit(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the words in the string, using sep as the delimiter string.
    
      sep
        The delimiter according which to split the string.
        None (the default value) means split according to any whitespace,
        and discard empty strings from the result.
      maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    
    Splits are done starting at the end of the string and working to the front.

>>> country="usa"
>>> correct_country=(country.upper())
>>> print(correct_country)
USA
>>> filename='hello.py'
>>> 'filename'.endswith('java')
False
>>> 'filename'.find('py'),.startswith('world')
SyntaxError: invalid syntax
>>> 'filename'.find('py')
-1
>>> 'filename'.startswith('world')
False
>>> 'filename'.find('lo')
-1
>>> help(stringmthods)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    help(stringmthods)
NameError: name 'stringmthods' is not defined
>>> help()

Welcome to Python 3.9's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> stringsmthods
No Python documentation found for 'stringsmthods'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> stringmethods
No Python documentation found for 'stringmethods'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> STRINGSMETHODS
No Python documentation found for 'STRINGSMETHODS'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> STRINGSMETHODS
No Python documentation found for 'STRINGSMETHODS'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> STRINGSMETHODS()
No Python documentation found for 'STRINGSMETHODS()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> HELP(STRINGSMETHODS)
No Python documentation found for 'HELP(STRINGSMETHODS)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> "STRINGSMETHODS'
No Python documentation found for '"STRINGSMETHODS\''.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 'MODULES STRINGSMETHODS'
No Python documentation found for 'MODULES STRINGSMETHODS'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 'topics stringsmethods'
No Python documentation found for 'topics stringsmethods'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.


>>> 
>>> 



>>> 
>>> quit()
>>> 