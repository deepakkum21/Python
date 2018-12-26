# Python OPPs
## Classes in Python
1. Python is an object oriented programming language. Unlike procedure oriented programming, where the main emphasis is on functions, object oriented programming stress on objects.
2. class is like a sketch (prototype) or blueprint of a house. It contains all the details about the floors, doors, windows etc. Based on these descriptions we build the house. House is the object.

## Defining a Class in Python
-               class MyNewClass:
                '''This is a docstring. I have created a new class'''
                    pass
- we define a class using the keyword class.                    
- The **first string is called docstring** and has a brief description about the class. It is an optional thing.
- A class **creates a new local namespace where all its attributes are defined**. Attributes may be data or functions.
- There are also special attributes in it that begins with double underscores (__ ). For example, `__doc__` gives us the docstring of that class.
- *As soon as we define a class, a new class object is created with the same name*. This class object allows us to access the different attributes as well as to instantiate new objects of that class.
-               class MyClass:
	                "This is my second class"
                    a = 10
                    def func(self):
                        print('Hello')

                # Output: 10
                print(MyClass.a)

                # Output: <function MyClass.func at 0x0000000003079BF8>
                print(MyClass.func)

                # Output: 'This is my second class'
                print(MyClass.__doc__)