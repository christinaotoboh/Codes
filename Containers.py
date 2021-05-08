Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #intergers, booleans and floats are all scalar types because they hold single values, hence they are known  as scalar values.
>>> name=list()  #list class
>>> name_1=[]  #list literal
>>> #You can prepopulate a list using any of the above(list class or literal) however the list class is redundant.
>>> name=list(["Micheal", "Samuel"])
>>> name_1=["Mich","Sammie"]
>>> type(name)
<class 'list'>
>>> type(name_1)
<class 'list'>
>>> print(name)
['Micheal', 'Samuel']
>>> list('Christy')
['C', 'h', 'r', 'i', 's', 't', 'y']
>>> list(17384)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list(17384)
TypeError: 'int' object is not iterable
>>> dir([])
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> couple=["Muina","Oni"]
>>> couple.append("Fred")
>>> print(couple)
['Muina', 'Oni', 'Fred']
>>> couple.append(263)
>>> print(couple)
['Muina', 'Oni', 'Fred', 263]
>>> id(couple)
2022144621824
>>> couple.append("Matt")
>>> id(couple)
2022144621824
>>> 
>>> print(couple)
['Muina', 'Oni', 'Fred', 263, 'Matt']
>>> id(couple)
2022144621824
>>> #Zero based indexing is the location of an item in a list.
>>> ingredient=["potatoes", "oil", "Salt"]
>>> #to access any of the item on the list we use the zero based index as shown below;
>>> ingredient[1]
'oil'
>>> ingredient[0]
'potatoes'
>>> #use the .insert method to insert an item at any index in a list. python shift all other items depending on the index see example below;
>>> ingredients.insert(3,"maggi")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ingredients.insert(3,"maggi")
NameError: name 'ingredients' is not defined
>>> ingredient.insert(3,"maggi")
>>> print(ingredient)
['potatoes', 'oil', 'Salt', 'maggi']
>>> ['potatoes', 'oil', 'Salt', 'maggi']
['potatoes', 'oil', 'Salt', 'maggi']
>>> #the syntax for replacement of an item in alist is the bracket notation[]
>>> ingredient[0]="yam"
>>> ingredient
['yam', 'oil', 'Salt', 'maggi']
>>> #use the .remove method to delete an item from a list, you can also use the bracket notation as will aslo be shown below
>>> ingredient.remove("yam")
>>> ingredient
['oil', 'Salt', 'maggi']
>>> del ingredient[2]
>>> ingredient
['oil', 'Salt']
>>> #sort list involves using the .sort method to sort items in a list
>>> ingredients.sort()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ingredients.sort()
NameError: name 'ingredients' is not defined
>>> ingredient.sort()
>>> ingredient
['Salt', 'oil']
>>> type(ingredient)
<class 'list'>
>>> old=[12,5,-7,30,-1]
>>> num_sorted=sorted(old)
>>> print(num_sorted)
[-7, -1, 5, 12, 30]
>>> print(old)
[12, 5, -7, 30, -1]
>>> #using the sorted function is a more general way of sorting sequence. It produces a new list which is sorted just as shown above.
>>> #You cant sort a list that contains heterogeneous items(i.e different types of items)
>>> #passing a key parameter to the .sort or sorted function allows control of the arbitary sorting.It could be callable by function, class, or method. this is applied when a list contains heterogeneous items.
>>> items=[1,4,0.6,"Amaka", "cbd"]
>>> items.sort(key=str)
>>> print(items)
[0.6, 1, 4, 'Amaka', 'cbd']
>>> new_items=sorted(items,key=int)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    new_items=sorted(items,key=int)
ValueError: invalid literal for int() with base 10: 'Amaka'
>>> dir([])
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> names=["a list above" {}.format("John")]
SyntaxError: invalid syntax
>>> names=["a list above {}".format("John")]
>>> names
['a list above John']
>>> type(names)
<class 'list'>
>>> names=["replace{John}".format("Christy")]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    names=["replace{John}".format("Christy")]
KeyError: 'John'
>>> num=range(5)
>>> list[num]
list[range(0, 5)]
>>> list(num)
[0, 1, 2, 3, 4]
>>> num=range(1,9)
>>> list(num)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> #the above built in function is the range function which is used to list a sequence of integer, it contains 3 parametrs of which 2 are optional(stride is the 3rd parameter which determines the sequences order of the intergers, example of the 3 parameters will be shown below)
>>> even=range(1,90,2)
>>> list(even)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89]
>>> even=range(,90,2)
SyntaxError: invalid syntax
>>> even=range(0,90,2)
>>> print(even)
range(0, 90, 2)
>>> list[even]
list[range(0, 90, 2)]
>>> list(even)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88]
>>> #half open interval convention
>>> a=range(0,5)
>>> b=range(5,10)
>>> both= list(a) + list(b)
>>> len(both)
10
>>> both
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(both)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> #len checks the length ok the list.
>>> 
>>> 
>>> #Tuples areimmutable ordered records that can not be changed once they are created. they are created using the literal syntax(using parentheses and commas in between them) or using the tuples class to create a a new tuple from an existing one.
>>> row=("George", "Mark")
>>> row
('George', 'Mark')
>>> type(row)
<class 'tuple'>
>>> ()
()
>>> tuple()
()
>>> #ways of creating empty tuples
>>> tuple([1])
(1,)
>>> a=(,1)
SyntaxError: invalid syntax
>>> tuple(,1)
SyntaxError: invalid syntax
>>> (1,)
(1,)
>>> one=(9,)
>>> type(one)
<class 'tuple'>
>>> #The above shows how to create a tuple with a single item using either the literal syntax or the tuple class.
>>> more=(1,"ada",8)
>>> type(more)
<class 'tuple'>
>>> dir([tuple])
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 
>>> #Sets are unordered sequences that uses the hash function. It is used to remove duplicates and check membership. Mutable objects such as list and dictionaries cannot be passed into a set because they are not hashable. ways to create a list includes passing a sequence into the set class or using the {} bracket to create the set. see below:
>>> digit=[0,1,1,2,3,4,5,6,7,8,9]
>>> new_digit=set(digit)
>>> new_digit
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> anon_digit={0,0,2,1,2,4,6,7,8}
>>> type(anon_digit)
<class 'set'>
>>> print(anon_digit)
{0, 1, 2, 4, 6, 7, 8}
>>> #to check membership use the in operator as in shown below
>>> 9 in new_digit
True
>>> 45 in anon_digit
False
>>> dir([set])
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> odd={1,3,5,7,9}
>>> Even=new_digit-odd
>>> print(even)
range(0, 90, 2)
>>> print(Even)
{0, 2, 4, 6, 8}
>>> type(Even)
<class 'set'>
>>> inter=new_digit&odd
>>> inter
{1, 3, 5, 7, 9}
>>> inter2=Even&anon_digit
>>> inter2
{0, 2, 4, 6, 8}
>>> inter3=anon_digit&odd
>>> inter3
{1, 7}
>>> number=Even|odd
>>> number
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> names={"Christy","Otoboh"}
>>> Christy in names
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    Christy in names
NameError: name 'Christy' is not defined
>>> "Christy" in names
True
>>> new=({"Jones"})
>>> type(new)
<class 'set'>
>>> tog=names|new
>>> tog
{'Christy', 'Otoboh', 'Jones'}
>>> tog-names
{'Jones'}
>>> tog&names
{'Christy', 'Otoboh'}
>>> tog&names
{'Christy', 'Otoboh'}
>>> 
>>> 
>>> 
>>> #Exercises
>>> 
>>> family=[]
>>> family.append("promise", "Margret", "Victor","Joshua","Ify")
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    family.append("promise", "Margret", "Victor","Joshua","Ify")
TypeError: list.append() takes exactly one argument (5 given)
>>> family=["Promise","Ify","Victor","Joshua","Mumsy","Me"]
>>> family
['Promise', 'Ify', 'Victor', 'Joshua', 'Mumsy', 'Me']
>>> family.sort
<built-in method sort of list object at 0x000001D6D13A01C0>
>>> family.sort()
>>> family
['Ify', 'Joshua', 'Me', 'Mumsy', 'Promise', 'Victor']
>>> new_family=sorted(family, key=str)
>>> new_family
['Ify', 'Joshua', 'Me', 'Mumsy', 'Promise', 'Victor']
>>> my_names=("Christiana","Otoboh", 27)
>>> type(my_names)
<class 'tuple'>
>>> people=[]
>>> people.append(my_names)
>>> people
[('Christiana', 'Otoboh', 27)]
>>> friend_1=("Deborah","Ezekiel",28)
>>> people.append(friend_1)
>>> people
[('Christiana', 'Otoboh', 27), ('Deborah', 'Ezekiel', 28)]
>>> friend_2=("Deborah", "onyegbunwa",24)
>>> people.append(friend_2)
>>> people
[('Christiana', 'Otoboh', 27), ('Deborah', 'Ezekiel', 28), ('Deborah', 'onyegbunwa', 24)]
>>> people.sort()
>>> people
[('Christiana', 'Otoboh', 27), ('Deborah', 'Ezekiel', 28), ('Deborah', 'onyegbunwa', 24)]
>>> people_new= sorted(people,0,key=str,reverse=False)
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    people_new= sorted(people,0,key=str,reverse=False)
TypeError: sorted expected 1 argument, got 2
>>> people_new= sorted(people,0,key=str)
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    people_new= sorted(people,0,key=str)
TypeError: sorted expected 1 argument, got 2
>>> people_new= sorted(people,key=str,reverse=False)
>>> people_new
[('Christiana', 'Otoboh', 27), ('Deborah', 'Ezekiel', 28), ('Deborah', 'onyegbunwa', 24)]
>>> people_new= sorted(people,key=int,reverse=False)
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    people_new= sorted(people,key=int,reverse=False)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> friends=["Deborah","Uche","Blessing","Onyinye","Chidinma","Chisom","Cynthia"]
>>> common_names=["Uche","Agnes", "Abigail","Onyinye", "Chisom","Cee","Honour","Jones","Love","Nene"]
>>> friends_new=set(friends)
>>> new_common=set(common_names)
>>> friends_new&new_common
{'Uche', 'Chisom', 'Onyinye'}
>>> new_common|friends_new
{'Cynthia', 'Honour', 'Nene', 'Chisom', 'Deborah', 'Abigail', 'Chidinma', 'Cee', 'Uche', 'Jones', 'Love', 'Blessing', 'Agnes', 'Onyinye'}
>>> common_new^friends_new
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    common_new^friends_new
NameError: name 'common_new' is not defined
>>> new_common^friends_new
{'Chidinma', 'Cee', 'Blessing', 'Love', 'Agnes', 'Cynthia', 'Honour', 'Nene', 'Deborah', 'Abigail', 'Jones'}
>>> shakes=
SyntaxError: invalid syntax
>>> shakes='''There is one point above all others which bears strongly against the theory that William Shakspere, of Stratford-on-Avon, was the author of the so-called Shakespeare’s Plays, and that is the audacious doggerel which has been fathered on his memory.  William Shakspere, after a disreputable youth, marrying at 17 or 18 a woman many years older than himself, whose child was soon after born, the son of a father who could not write his name, and in debt and difficulty, and who himself (père) had been within the clutches of the law, found his native place too hot to hold him, and if the universal tradition on the subject is worth anything, having a warrant out against him for poaching, “flitted” to London, became a stage-player, went in for speculation in building a theatre, laid out his modest earnings judiciously, bought a house in his native place, another in London “within the precinct of the late Black Fryers,” retired to New Place, died, and was buried in the church of that dirty town, in p. 61616, in the chancel, and his epitaph inscribed at his request upon his tomb.  He appears to have been in the habit of writing or quoting such, and got the credit for this sort of poetry from his companions.  It is plain from the evidence I produce (p. 7) that in and about those years it was the custom in London churches to put verses of questionable merit on monuments and tombs, that it was usual to “crib” or copy them from some one else, and use them as their own.  The instances I give (and their name is legion) shows this clearly to have been an every-day practice.  The play-actor, with a memory sharpened “by learning his parts,” had no doubt seen them on the walls of churches during his residence in London, and was in the habit of repeating and passing off as his own these doggerel rhymes for the edification and amusement of his companions and select friends; but when asked to give them an extempore one (evidently there was a leetle doubt as to his powers of composition), knocked off one or two much inferior to those his memory had retained (p. 11).  What a specimen of their high literary taste and also of his own, requesting to have such rubbish inscribed upon his grave!  No doubt there were many other such-like epitaphs in churches in London which have been destroyed or effaced by lapse of time, but these are a sufficient specimen to show how little variation there is in them, and that mainly in the spelling.  The epitaph on the stone over Shakspere’s grave has been pressed into the service by a believer in his writings to prove—first, that he “curst those who should move his bones,” because that he was fearful that when his renown was acknowledged, his bones would be moved from their last resting-place in the Stratford that he loved, p. 7to find a grave (they have a monument) in Westminster Abbey! and secondly, by a non-believer, that when the imposture was found out, they would be exhumed and cast out to the four winds of heaven!  But how about poor “Virginea optima vita El. 21,” whose Covent Garden grave had on its surface the same curse “for he that moves my bones”?  Did her people fear that some after-scandal might occur to show that she was no better than Ann Hathway or Jane Shore, and her ashes be scattered in the swollen flood of the Fleet stream! or that an unknown princess or poetess unrecognised, cared not for a niche in Poet’s Corner or a sepulchre amongst the great ones of the land, should her real self and character ever be found out!  In searching for epitaphs of a similar style I found the following, which I give as illustrative of what I have mentioned above.  They are extracted from an ancient folio, 1736 A.D., The History of London, by William Maitland, F.R.S., which gives an account of the several parishes and churches.'''
>>> parag='It chanced during one winter, a few years ago, that our cities were bent on discussing the theory of the Age. By an odd coincidence, four or five noted men were each reading a discourse to the citizens of Boston or New York, on the Spirit of the Times. It so happened that the subject had the same prominence in some remarkable pamphlets and journals issued in London in the same season. To me, however, the question of the times resolved itself into a practical question of the conduct of life. How shall I live? We are incompetent to solve the times. Our geometry cannot span the huge orbits of the prevailing ideas, behold their return, and reconcile their opposition. We can only obey our own polarity.'
>>> shakes.split(sep=, maxsplit=10)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> shakes.split(, 10)
SyntaxError: invalid syntax
>>> shakes.split()
['There', 'is', 'one', 'point', 'above', 'all', 'others', 'which', 'bears', 'strongly', 'against', 'the', 'theory', 'that', 'William', 'Shakspere,', 'of', 'Stratford-on-Avon,', 'was', 'the', 'author', 'of', 'the', 'so-called', 'Shakespeare’s', 'Plays,', 'and', 'that', 'is', 'the', 'audacious', 'doggerel', 'which', 'has', 'been', 'fathered', 'on', 'his', 'memory.', 'William', 'Shakspere,', 'after', 'a', 'disreputable', 'youth,', 'marrying', 'at', '17', 'or', '18', 'a', 'woman', 'many', 'years', 'older', 'than', 'himself,', 'whose', 'child', 'was', 'soon', 'after', 'born,', 'the', 'son', 'of', 'a', 'father', 'who', 'could', 'not', 'write', 'his', 'name,', 'and', 'in', 'debt', 'and', 'difficulty,', 'and', 'who', 'himself', '(père)', 'had', 'been', 'within', 'the', 'clutches', 'of', 'the', 'law,', 'found', 'his', 'native', 'place', 'too', 'hot', 'to', 'hold', 'him,', 'and', 'if', 'the', 'universal', 'tradition', 'on', 'the', 'subject', 'is', 'worth', 'anything,', 'having', 'a', 'warrant', 'out', 'against', 'him', 'for', 'poaching,', '“flitted”', 'to', 'London,', 'became', 'a', 'stage-player,', 'went', 'in', 'for', 'speculation', 'in', 'building', 'a', 'theatre,', 'laid', 'out', 'his', 'modest', 'earnings', 'judiciously,', 'bought', 'a', 'house', 'in', 'his', 'native', 'place,', 'another', 'in', 'London', '“within', 'the', 'precinct', 'of', 'the', 'late', 'Black', 'Fryers,”', 'retired', 'to', 'New', 'Place,', 'died,', 'and', 'was', 'buried', 'in', 'the', 'church', 'of', 'that', 'dirty', 'town,', 'in', 'p.', '61616,', 'in', 'the', 'chancel,', 'and', 'his', 'epitaph', 'inscribed', 'at', 'his', 'request', 'upon', 'his', 'tomb.', 'He', 'appears', 'to', 'have', 'been', 'in', 'the', 'habit', 'of', 'writing', 'or', 'quoting', 'such,', 'and', 'got', 'the', 'credit', 'for', 'this', 'sort', 'of', 'poetry', 'from', 'his', 'companions.', 'It', 'is', 'plain', 'from', 'the', 'evidence', 'I', 'produce', '(p.', '7)', 'that', 'in', 'and', 'about', 'those', 'years', 'it', 'was', 'the', 'custom', 'in', 'London', 'churches', 'to', 'put', 'verses', 'of', 'questionable', 'merit', 'on', 'monuments', 'and', 'tombs,', 'that', 'it', 'was', 'usual', 'to', '“crib”', 'or', 'copy', 'them', 'from', 'some', 'one', 'else,', 'and', 'use', 'them', 'as', 'their', 'own.', 'The', 'instances', 'I', 'give', '(and', 'their', 'name', 'is', 'legion)', 'shows', 'this', 'clearly', 'to', 'have', 'been', 'an', 'every-day', 'practice.', 'The', 'play-actor,', 'with', 'a', 'memory', 'sharpened', '“by', 'learning', 'his', 'parts,”', 'had', 'no', 'doubt', 'seen', 'them', 'on', 'the', 'walls', 'of', 'churches', 'during', 'his', 'residence', 'in', 'London,', 'and', 'was', 'in', 'the', 'habit', 'of', 'repeating', 'and', 'passing', 'off', 'as', 'his', 'own', 'these', 'doggerel', 'rhymes', 'for', 'the', 'edification', 'and', 'amusement', 'of', 'his', 'companions', 'and', 'select', 'friends;', 'but', 'when', 'asked', 'to', 'give', 'them', 'an', 'extempore', 'one', '(evidently', 'there', 'was', 'a', 'leetle', 'doubt', 'as', 'to', 'his', 'powers', 'of', 'composition),', 'knocked', 'off', 'one', 'or', 'two', 'much', 'inferior', 'to', 'those', 'his', 'memory', 'had', 'retained', '(p.', '11).', 'What', 'a', 'specimen', 'of', 'their', 'high', 'literary', 'taste', 'and', 'also', 'of', 'his', 'own,', 'requesting', 'to', 'have', 'such', 'rubbish', 'inscribed', 'upon', 'his', 'grave!', 'No', 'doubt', 'there', 'were', 'many', 'other', 'such-like', 'epitaphs', 'in', 'churches', 'in', 'London', 'which', 'have', 'been', 'destroyed', 'or', 'effaced', 'by', 'lapse', 'of', 'time,', 'but', 'these', 'are', 'a', 'sufficient', 'specimen', 'to', 'show', 'how', 'little', 'variation', 'there', 'is', 'in', 'them,', 'and', 'that', 'mainly', 'in', 'the', 'spelling.', 'The', 'epitaph', 'on', 'the', 'stone', 'over', 'Shakspere’s', 'grave', 'has', 'been', 'pressed', 'into', 'the', 'service', 'by', 'a', 'believer', 'in', 'his', 'writings', 'to', 'prove—first,', 'that', 'he', '“curst', 'those', 'who', 'should', 'move', 'his', 'bones,”', 'because', 'that', 'he', 'was', 'fearful', 'that', 'when', 'his', 'renown', 'was', 'acknowledged,', 'his', 'bones', 'would', 'be', 'moved', 'from', 'their', 'last', 'resting-place', 'in', 'the', 'Stratford', 'that', 'he', 'loved,', 'p.', '7to', 'find', 'a', 'grave', '(they', 'have', 'a', 'monument)', 'in', 'Westminster', 'Abbey!', 'and', 'secondly,', 'by', 'a', 'non-believer,', 'that', 'when', 'the', 'imposture', 'was', 'found', 'out,', 'they', 'would', 'be', 'exhumed', 'and', 'cast', 'out', 'to', 'the', 'four', 'winds', 'of', 'heaven!', 'But', 'how', 'about', 'poor', '“Virginea', 'optima', 'vita', 'El.', '21,”', 'whose', 'Covent', 'Garden', 'grave', 'had', 'on', 'its', 'surface', 'the', 'same', 'curse', '“for', 'he', 'that', 'moves', 'my', 'bones”?', 'Did', 'her', 'people', 'fear', 'that', 'some', 'after-scandal', 'might', 'occur', 'to', 'show', 'that', 'she', 'was', 'no', 'better', 'than', 'Ann', 'Hathway', 'or', 'Jane', 'Shore,', 'and', 'her', 'ashes', 'be', 'scattered', 'in', 'the', 'swollen', 'flood', 'of', 'the', 'Fleet', 'stream!', 'or', 'that', 'an', 'unknown', 'princess', 'or', 'poetess', 'unrecognised,', 'cared', 'not', 'for', 'a', 'niche', 'in', 'Poet’s', 'Corner', 'or', 'a', 'sepulchre', 'amongst', 'the', 'great', 'ones', 'of', 'the', 'land,', 'should', 'her', 'real', 'self', 'and', 'character', 'ever', 'be', 'found', 'out!', 'In', 'searching', 'for', 'epitaphs', 'of', 'a', 'similar', 'style', 'I', 'found', 'the', 'following,', 'which', 'I', 'give', 'as', 'illustrative', 'of', 'what', 'I', 'have', 'mentioned', 'above.', 'They', 'are', 'extracted', 'from', 'an', 'ancient', 'folio,', '1736', 'A.D.,', 'The', 'History', 'of', 'London,', 'by', 'William', 'Maitland,', 'F.R.S.,', 'which', 'gives', 'an', 'account', 'of', 'the', 'several', 'parishes', 'and', 'churches.']
>>> parag.split(10)
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    parag.split(10)
TypeError: must be str or None, not int
>>> parag.split()
['It', 'chanced', 'during', 'one', 'winter,', 'a', 'few', 'years', 'ago,', 'that', 'our', 'cities', 'were', 'bent', 'on', 'discussing', 'the', 'theory', 'of', 'the', 'Age.', 'By', 'an', 'odd', 'coincidence,', 'four', 'or', 'five', 'noted', 'men', 'were', 'each', 'reading', 'a', 'discourse', 'to', 'the', 'citizens', 'of', 'Boston', 'or', 'New', 'York,', 'on', 'the', 'Spirit', 'of', 'the', 'Times.', 'It', 'so', 'happened', 'that', 'the', 'subject', 'had', 'the', 'same', 'prominence', 'in', 'some', 'remarkable', 'pamphlets', 'and', 'journals', 'issued', 'in', 'London', 'in', 'the', 'same', 'season.', 'To', 'me,', 'however,', 'the', 'question', 'of', 'the', 'times', 'resolved', 'itself', 'into', 'a', 'practical', 'question', 'of', 'the', 'conduct', 'of', 'life.', 'How', 'shall', 'I', 'live?', 'We', 'are', 'incompetent', 'to', 'solve', 'the', 'times.', 'Our', 'geometry', 'cannot', 'span', 'the', 'huge', 'orbits', 'of', 'the', 'prevailing', 'ideas,', 'behold', 'their', 'return,', 'and', 'reconcile', 'their', 'opposition.', 'We', 'can', 'only', 'obey', 'our', 'own', 'polarity.']
>>> shakes_new=set(shakes)
>>> parag_new=set(parag)
>>> shakes_new&parag_new
{'u', 'S', 'o', 'a', '?', 'm', 'k', 'y', 'I', 'g', 'c', 'N', 'i', 'H', 'W', 'v', ' ', 'l', 'A', 'b', 'L', 's', 'f', ',', 'h', 'e', '.', 'B', 'j', 'q', 'r', 'T', 'p', 'n', 't', 'd', 'w'}
>>> a=parag.split()
>>> 