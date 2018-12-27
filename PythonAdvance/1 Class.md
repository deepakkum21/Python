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

                # This gives all the info about the class
                help(MyClass)

## Objects in Python     
1. Object is simply a collection of data (variables) and methods (functions) that act on those data. And, class is a blueprint for the object.
2. An object is also called an instance of a class and the process of creating this object is called instantiation.

## Creating an Object in Python
- class object could be used to access different attributes.
- Class can also be used to create new object instances (instantiation) of that class. The procedure to create an object is similar to a function call.
                `       obj = MyClass()    `
- This will create a new instance object named obj. We can access attributes of objects using the object name prefix.
- Attributes may be data or method. Method of an object are corresponding functions of that class.
- Any function object that is a class attribute defines a method for objects of that class.
- This means to say, since **MyClass.func is a function object (attribute of class), ob.func will be a method object**.
-               class MyClass:
                    "This is my second class"
                    a = 10
                    def func(self):
                        print('Hello')

                # create a new MyClass
                ob = MyClass()

                # Output: <function MyClass.func at 0x000000000335B0D0>
                print(MyClass.func)

                # Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
                print(ob.func)

                # Calling function func()
                # Output: Hello
                ob.func()

## self parameter in function definition inside the class
- self parameter in function definition inside the class but, we called the method simply as ob.func() without any arguments. It still worked.
- This is because, **whenever an object calls its method, the object itself is passed as the first argument. So, ob.func() translates into MyClass.func(ob)**.
- In general, **calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method's object before the first argument.**
- For the above reasons, the **first argument of the function in class must be the object itself**. 
- self is the reference variable that is always pointing to the current object.
- Within the python class to refer current object we should use self variable.
- the first argument to constructor or instance method should be self variable.
- PVM (Python Virtual Machine) is responsible to provide value for self argument and we are not required to provide expicitly.
- By using self we can declare  instance variable.
- By using self we can access  instance variable.
- Instead of self we can use any name, but ..... self is recommended to use

## Constructors in Python
- Class functions that begins with double underscore `( __ )` are called special functions as they have special meaning.
- `__init__()` function is special **function gets called whenever a new object of that class is instantiated**.
- The name should always be `__init___()`
- Whenever we are **creating an object constructor will be executed automatically** and we are not required to call explicitly.
- Objective:- is to **declare and initailize instance variable**.
- We can **declare multiple constructor but the PVM is only going to consider the last declared constructor** because method overloading or constructor overloading facility is not present in python.
- For **every object the constructor will be exeuted only once**.
-               class ComplexNumber:
                    def __init__(self,r = 0,i = 0):
                        self.real = r
                        self.imag = i

                    def getData(self):
                        print("{0}+{1}j".format(self.real,self.imag))

                # Create a new ComplexNumber object
                c1 = ComplexNumber(2,3)

                # Call getData() function
                # Output: 2+3j
                c1.getData()

                # Create another ComplexNumber object
                # and create a new attribute 'attr'
                c2 = ComplexNumber(5)
                c2.attr = 10

                # Output: (5, 0, 10)
                print((c2.real, c2.imag, c2.attr))

                # but c1 object doesn't have attribute 'attr'
                # AttributeError: 'ComplexNumber' object has no attribute 'attr'
                c1.attr

| **Method** | **Constructor** |                                                                                                        
| ---------- | --------------- |                                                                                   
| The name can be anything. | The name should be `__init__()` |
| It is will executed if we call |  It is will executed automatically, Whenever we are creating an object | 
| It can be called any no of times for an particular object | It will be called only once for an object |
| It is used to implement business logic | It is used to declare and initailize instance variable |   

## Types of variables:-
1. Instance variables / object level variables
2. Static variables / class level variables
3. Local variables / method level variables
4. global variable

## Types of methods:
1. instance method / object releated method
2. class methods / class level methods
3. static methods / utility methods


## ClassLevel Method:-
- Class method can be used when we are only using static variable and not instance variable.
-               class MyClass:
                    ''' This class is regarding class method'''
                    collegeName = 'ABC'         # static variable
                    @classmethod
                    def getCollegeName(cls):
                        print('CollegeName: ' + cls.collegeName)

                    MyClass.getCollegeName()    # class method can be called using className

## Static Method:-
- static method can be used when we are not using both static variable and instance variable.
-               class MyClass:
                    ''' This class is regarding static method'''
                    collegeName = 'ABC'
                    @staticmethod
                    def findAverage(a, b):
                        print('Average: ' + (a+b)/2)

                    obj = MyClass()
                    obj.findAverage(4,5)        # static method can be called using obj ref
                    MyClass.findAverage(5,6)    # static method can be called using className


| **instance method** | **classLevel method** | **static method** |                                                                                  
| ------------------- | --------------------- | ----------------- |                                                                 
| Inside method body if we are using atleast one instance var then it is compulsory to use instance method | Inside method body if we are using only static variable   then it is highly recommended to use classLevel method   (@classmethod) | Inside method body if we are not using any static variable and instance var then it is highly recommended to use static method , to define general utility method |
| no need to use any decorator | decorator is used to declare a class level method (@classmethod) | deocrator is optional, recommended to use (@staticmethod) |
| The 1st argument to instance method should be the self, which is the reference to the current obj to access the instance variable | The 1st argument to class level method should be the  **cls**, which is the reference to the current class object by using that we can access the static var | It may or may not have any arg depending on the usage we can have arg |
| inside instance method we can access both static and instance var | inside class level method we can only access static var, not instance var | it is used only incase when we are not using any of the instance and static var, then no point of accessing any one of them |
| can call instance method by using objref | can call class level method by using objref and className, but recommended to use className | can call static method by using objref and className, but recommended to use className |


## Getters and setters :-
- *setters*
    -            class MySetters:
                    ''' Demonstrates setters'''
                    def __init__(self, name, age):
                        self.name = name
                        self.age = age
                    def setName(self, name):
                        self.name = name
                    def setAge(self, age):
                        self.age = age
- *getters*
    -            class MyGetters:
                    ''' Demonstrates getters'''
                    def __init__(self, name, age):
                        self.name = name
                        self.age = age
                    def setName(self):
                        return self.name
                    def setAge(self):
                        return self.age