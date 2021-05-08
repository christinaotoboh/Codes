Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_str='\this is a string with backlash\\'
>>> my_str
'\this is a string with backlash\\'
>>> my_str=('\\this is a string with backlash\\')
>>> my_str
'\\this is a string with backlash\\'
>>> print(my_str)
\this is a string with backlash\
>>> an_str=r'\\This is another string with backlash but raw string\\'
>>> print(an_str)
\\This is another string with backlash but raw string\\
>>> #Use r as an alternative to escape sequence(\) however it gives a literal interpretation to your string.
>>> 
>>> 
>>> #triple quotes mechanisms(''' ''') are used for strings that contains multiple lines or paragraphs. They are also used in writing Docstrings.
>>> '''this is a multiple line of string that contains multiple lines and strings, however we dont know if it runs on its on'''
'this is a multiple line of string that contains multiple lines and strings, however we dont know if it runs on its on'
>>> """This string has multiple lines as shown below
....This is the second line
....This is the third line
....This is the fourth line
....This is the final line"""
'This string has multiple lines as shown below\n....This is the second line\n....This is the third line\n....This is the fourth line\n....This is the final line'
>>> 'This string has multiple lines as shown below\n....This is the second line\n....This is the third line\n....This is the fourth line\n....This is the final line'
'This string has multiple lines as shown below\n....This is the second line\n....This is the third line\n....This is the fourth line\n....This is the final line'
>>> a="""This string has multiple lines as shown below
....This is the second line
....This is the third line
....This is the fourth line
....This is the final line"""
>>> print(a)
This string has multiple lines as shown below
....This is the second line
....This is the third line
....This is the fourth line
....This is the final line
>>> a="This string has multiple lines as shown below
....This is the second line
....This is the third line
....This is the fourth line
....This is the final line"
SyntaxError: EOL while scanning string literal
>>> #The above code proves that we cannot write multiple lines of strings with single or double but with triple quotes
>>> """He said, "Hello"""
'He said, "Hello'
>>> """ He said, "Hello\""""
' He said, "Hello"'
>>> """he said, "hello""""
SyntaxError: EOL while scanning string literal
>>> 
>>> #Formating strings use {}.format(placeholder)
>>> the_name="Christy"
>>> print("Hello"{}.format(the_name))
SyntaxError: invalid syntax
>>> print("Hello{}".format(the_name))
HelloChristy
>>> print("Hello{}",.format(the_name))
SyntaxError: invalid syntax
>>> print("Hello{},".format(the_name))
HelloChristy,
>>> print("Hello{}" .format(the_name))
HelloChristy
>>> print("Hello {}".format(the_name))
Hello Christy
>>> #.format can also be used for formatting numbers too.
>>> a=('a {}'.format(2),'b {}'.format(4),'c {}'.format(6),'d {}'.format(:4))
SyntaxError: invalid syntax
>>> a=('a {}'.format(2),'b {}'.format(4),'c {}'.format(6),'d {}'.format(4))
>>> a
('a 2', 'b 4', 'c 6', 'd 4')
>>> a=('a :{}'.format(2),'b :{}'.format(4),'c :{}'.format(6),'d :{}'.format(:4))
SyntaxError: invalid syntax
>>> a=('a {}'.format(2),'b {}'.format(4),'c {}'.format(6),'d {}'.format(:4))
SyntaxError: invalid syntax
>>> a=('a :{}'.format(2),'b :{}'.format(4),'c :{}'.format(6),'d :{}'.format(4))
>>> a
('a :2', 'b :4', 'c :6', 'd :4')
>>> print('a:{} b:{} c:{}'.format(1,2,3))
a:1 b:2 c:3
>>> 