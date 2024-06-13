#========================data Types=========================
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType
#========================data Types===========================
x = 1
y = 2.8
z = 1j

# print(type(x))<class 'int'>
# print(type(y))<class 'float'>
# print(type(z))<class 'complex'>

#=====casting===========================================================
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#========Strings=================================================
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

#================================================================
for x in "banana":
  print(x)

print(len(a))

txt = "The best things in life are free!"
print("free" in txt) #True
print("expensive" not in txt)

#======slicing==========================================================
b = "Hello, World!"
print(b[:5]) #Hello
print(b[2:]) #llo, World!
print(b[-5:-2]) #orl
print(a.upper())
print(a.lower())
print(a.strip()) 
print(a.replace("H", "J"))
print(a.split(","))


age = 36
txt = f"My name is John, I am {age}"

#==========List=========================================================
mylist = ["apple", "banana", "cherry"]
print(len(thislist))
thislist.remove("banana")
thislist.pop(1)
del thislist[0]
del thislist
thislist.clear()


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[i])

[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in range(10) if x < 5]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]

thislist = [100, 50, 65, 82, 23]
thislist.sort()
thislist.sort(reverse = True)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)

#copy
mylist = thislist.copy()
mylist = list(thislist)


#================================================================
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#======tuple==========================================================
#Tuple items are ordered, unchangeable, and allow duplicate values.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")

#=============================================================
if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
if not a > b:
  
for x in fruits:
  if x == "banana":
    continue
  print(x)

#============functions===============================================
def my_function():
  print("Hello from a function")

my_function()

# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#======classes==========================================================
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#================================================================
# The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)

#===json================================================
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



# convert into JSON:
y = json.dumps(x)

#=========date===========================================
import datetime

x = datetime.datetime.now()

print(x.year)#2024
print(x.strftime("%A"))#Wednesday

# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character	%	
# %G	ISO 8601 year	2018	
# %u	ISO 8601 weekday (1-7)	1	
# %V	ISO 8601 weeknumber (01-53)	01
