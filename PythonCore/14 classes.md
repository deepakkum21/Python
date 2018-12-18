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
                 def method_class(self):                                    
                     self.d=40       (static var)                                   
                     className.e=50       (static var)        
    - by using static method
        -        @staticmethod                                                                                          
                 def method_name():                                                                
                     className.var=value   
    - outside the class using className.var= value                                               
5. **modification of static var**
    - either by using className or by self if it is in class method(havung @classmethod anotation)
    - but not using objref or by using self in instance method (infact this will lead in creation of instance var)

## Copy in Python 
sometimes we may want to have the original values unchanged and only modify the new values or vice versa. In Python, there are two ways to create copies:
- Shallow Copy(.copy(arg))
- Deep Copy (.deepcopy(arg))
(https://www.programiz.com/python-programming/shallow-deep-copy)

### Shallow Copy and Deep copy
1. **shallow copy**   
    - If the original object contains any references to mutable objects, just duplicate  refrence variable will be created pointing to the old contained objects, but not duplicate object creation
    - A shallow copy creates a new object which stores the reference of the original elements.
    - So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. 
    - This copy process does not recurse or create copies of nested objects itself.
        -               import copy                                                                                               
                        old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]                                                                     
                        new_list = copy.copy(old_list)                                                                             
                        print("Old list:", old_list)                                                                    
                        print("New list:", new_list)
                        old_list[0][1] = 5
                        print("Old list after changes:", old_list)
                        print("New list after changes in old list:", new_list)

2. **Deep Copy**
    - A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
    - The deep copy creates independent copy of original object and all its nested objects.
        -               import copy                                                                                               
                        old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]                                                                     
                        new_list = copy.copy(old_list)                                                                             
                        print("Old list:", old_list)                                                                    
                        print("New list:", new_list)