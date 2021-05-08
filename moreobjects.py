#id shows position of an object in the computer RAM
#name="Christy"
#print(id(name))
#first=name
#print(id(first))

#use 'is' to do identity check for 2 variables having the same object
#name is first
#name='Fred'
#print(id(name))

#object type allows you to view the data state and the action it performs.it is the class of the object.
#type(name)
#type(first)
#inte=34
#type(inte)

#Mutable objects can change their values but their id stays the same e.g list and dictionary
#names=[]
#print(names)
#print(id(names))
#names.append("CJ")
#print(id(names))

#immutable objects like int, floats, str cannot change their states, however if their values are changed their id also changes
#age=100
#print(age)
#print(id(age))
#age=age+10
#print(age)
#print(id(age))


#Exercise

a=20.10
print(a)
id(a)
type(a)

a=a+20
id(a)
type(a)

games=[]
print(games)
id(games)
type(games)
games.append("Sudoku")
id(games)
type(games)



