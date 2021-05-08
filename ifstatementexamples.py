Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> year=2021
>>> if year%4=0:
	
SyntaxError: invalid syntax
>>> if year%==0:
	
SyntaxError: invalid syntax
>>> if year%4==0:
	print("year is a leap year")
else:
	print("not a leap year")

	
not a leap year
>>> odd_no=57
>>> if odd_no%2==1:
	print("This is an odd no")
else:
	print("This is an even number!")

	
This is an odd no
>>> if 3>4:
      print("great")
 else:
	 
SyntaxError: unindent does not match any outer indentation level
>>> 