def greeting(name):
    return f"hello {name} how was last night?"
print(greeting("Monica"))

#f-strings in Python
def introduce (name, age):
  return f"Hello, my name is {name} and am {age} years old."
print (introduce ("Merine", 30))

'''
Arbitrary parameters
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

Example
If the number of arguments is unknown, add a * before the parameter name:

#This way the function will receive a tuple of arguments, and can access the items accordingly:

'''

def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")


#Passing a List as an Argument


def favourite(food):
  for fruit in food:
    print (fruit)
fruit =("mangoes", "avocado","apples")
favourite(fruit)

'''
Return Values
To let a function return a value, use the return statement:
'''
def multiply(value):
  return 5 * value
print(multiply(5))
'''
The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

'''
def empty(value):
    pass

'''
Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:
'''

def foodie(fruit = "Avocado"):
    print("My favourite fruit is " + fruit) 

foodie("Pineapple")
foodie("Melon")
foodie()
foodie("Banana")


'''
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

Example
If the number of arguments is unknown, add a * before the parameter name:

'''

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

'''
Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.
'''
def contract(name, age):
    return f"New employee is {name} and he is {age} years old"
print(contract(name="mark", age = 29))

'''
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

Example
If the number of keyword arguments is unknown, add a double ** before the parameter name:


'''

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#Arbitrary Arguments, *args

def feel (*fruits):
    for f in fruits:
        print(f)
feel("Mango", "kiwi", "Ban")



  # So for the below its a tuple - data type -for arbitary parameters

def feel (*fruits):
    for i in fruits:
       print (i)
feel("Mango", "Avocado", "Sugarcane")


def feel (**fruits):
   for key in fruits:
       print (fruits[key])
feel(Mango=32, Avocado=23,  sugarcane=34)


#program for recussive function

def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))  