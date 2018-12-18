# Classes

| **Constructor** |  **method** |                                                                                   
| --------------- | ----------- |                                                                                             
| name should be __ init__ | any name can be for the method |
| will be executed automatically whenever we are creating object | will we executed whenever we call that method |
| per object this will be executed only once | per object the method can be called any no of times |
| generally it is used to declare and initialize instance variables | inside we can write business logic | 
| syntax :-  def __ init__(self,arguments):  self.instance_var=value | syntax :- def methodName(self,arg): logic | 

## Types of variables:
- instance variable(non-static)
- static variable
- local variable

### Instance Variable:-
1. it should be used if the value of the variable is to be varied from object to object
2. for every object a separate copy will be created if the instance variable will be created
3. In general, inside constructor instance varaible are declared. 
4. Access instance variable:-
    - inside calss => by using self
    - outside class => by using reference 
5. Objectreferenece.__ dict__    =>   return the dict having instance variable with value
6. **places where to declare**
    - inside constructor
    - inside instance method
    - outside class using ref var

### Static variable
1. it should be used if the value of the varible has to be same for all the objects of that class
2. for every object same copy will be assigned
3. In general, within class static variable is declared
4. **places to declare**
    - within the class directly
    - inside contructor by using class name
    - inside instance method by using class name
    - by using class method
        -        @classmethod
        -        def method_class(self):
        -            self.d=40       (static var)
        -            className.e=50       (static var)
    - by using static method
        -        @staticmethod
        -        def method_name():
        -            className.var=value

    