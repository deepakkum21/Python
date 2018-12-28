# Inheritance 
1. It refers to defining a new class with little or no modification to an existing class. 
2. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.
3. Syntax:-
    -               class BaseClass:
                        Body of base class

                    class DerivedClass(BaseClass):
                        Body of derived class
4. Derived class inherits features from the base class, adding new features to it. This results into **re-usability of code**.


| **Composition** | **Aggregation** |
| --------------- | --------------- |                                                                        
| Strong Association | Weak association |
| Without you i can not be there | without you i can be |
| Has-A relation |   Has-A relation |   
| relaion between class and static var | relaion between Object and instance var |

## Types of Inheritance
- Single Inheritance
- Multi level Inheritance
- Multiple Inheritance
- Hierarchical Inheritance
- Hybrid Inheritance

1. **Single Inheritance in Python**
- A single Python inheritance is when a single class inherits from a class.
-                   class Parent:
                        def m1(self):
                            print('Parent method')
                        
                    class Child(Parent);
                        def m2(self):
                            print('Child method')
                    
                    child = Child()
                    child.m1()
                    child.m2()

-                   x=0
                    class fruit:
                        def __init__(self):
                            global x
                            x+=1
                            print("I'm a fruit")                                                  
                    class citrus(fruit):
                        def __init__(self):
                            super().__init__()
                            global x
                            x+=2
                            print("I'm citrus") 

                    lime = Citrus()

2. **Python Multiple Inheritance**
- When a there are multiple parent classes for a single child
-                   class Base1:
                        pass

                    class Base2:
                        pass

                    class MultiDerived(Base1, Base2):
                        pass

-                   class Parent1:
                        def m1(self):
                            print('Parent1 method')

                    class Parent2:
                        def m1(self):
                            print('Parent2 method')
                        
                    class Child(Parent1, Parent2);
                        def m2(self):
                            print('Child method')
                    
                    child = Child()
                    child.m1()
                    child.m2() 

- **To solve the problem of ambiguity in multiple inheritance**
    1. First the desired method is searched in the respective classes and if not present then they follow a order,
    2. The method are searched in the order in which the parent class is inherited eg. if Parent1 comes first then the method will be searched in Parent1 class and if it is not able to find then it will search in the next Parent class which is next to the Parent1 class  .                    

3. **Multilevel Inheritance**
- When one class inherits from another, which in turn inherits from another.
-                   class Parent:
                        def m1(self):
                            print('Parent method')
                        
                    class Child(Parent);
                        def m2(self):
                            print('Child method')

                    class SubChild(Child);
                        def m3(self):
                            print('SubChild method')
                    
                    subchild = SubChild()
                    subchild.m1()
                    subchild.m2()
                    subchild.m3()

4. **Hierarchical Inheritance**
- When a parent class is inherited in more than 1 child class
-                   class Parent:
                        def m1(self):
                            print('Parent method')
                        
                    class Child1(Parent);
                        def m2(self):
                            print('Child1 method')

                    class Child2(Child);
                        def m3(self):
                            print('Child2 method')
                    
                    child1 = Child1()
                    child1.m1()
                    child1.m2()
                    child2 = Child2()
                    child2.m1()
                    child2.m3()

5. **Hybrid Inheritance**
- combination of any two kinds of inheritance


## Method Resolution Operator(MRO)
1. Every class in Python is derived from the class object. **object class is the most base type** in Python.
2. all other class, either built-in or user-defines, are derived classes and all objects are instances of object class.
3.                  # Output: True
                    print(issubclass(list,object))

                    # Output: True
                    print(isinstance(5.5,object))

                    # Output: True
                    print(isinstance("Hello",object))
4. **Follows depth-first, left-right fashion without searching same class twice.**                    
5. MRO of a class can be viewed as the `__mro__` attribute or `mro()` method.
6.                  class X: pass
                    class Y: pass
                    class Z: pass

                    class A(X,Y): pass
                    class B(Y,Z): pass

                    class M(B,A,Z): pass

                    # Output:
                    # [<class '__main__.M'>, <class '__main__.B'>,
                    # <class '__main__.A'>, <class '__main__.X'>,
                    # <class '__main__.Y'>, <class '__main__.Z'>,
                    # <class 'object'>]

                    print(M.mro())      # print(M.__mro___)

7. Uses **C3 algorithm**
-                   class A:
                        pass
                    class B:
                        pass
                    class C:
                        pass
                    class X(A, B):
                        pass
                    class Y(B, C):
                        pass
                    class P(X, Y, C):
                        pass
                    
                    print(P.mro())
- If  ABCDE then, **A -> Head & BCDE -> tail**
- **if head element of First list is not present in the tail part of any other list then consider that element in the result and remove that element from all the list .**
- One clue **Object will always be the last in the MRO list**
- The algorithm says 
    -       mro(P)  = P + Merge(mro(immediate parents) + Parentlist)
                    = P + Merge(mro(X), mro(Y), mro(C), XYC)
                    = P + Merge(XABO, YBCO, CO, XYC)
                    = P + X + Merge(ABO, YBCO, CO, YC)
                    = P + X + A + Merge(BO, YBCO, CO, YC)
                    = P + X + A + Merge(BO, YBCO, CO, YC)   { B is present in the tail part so leave that list check other list}
                    = P + X + A + Y + Merge(BO, BCO, CO, C)
                    = P + X + A + Y + B + Merge(O, CO, CO, C)    { O is present in the tail part so leave that list check other list}
                    = P + X + A + Y + B + Merge(O, CO, CO, C)
                    = P + X + A + Y + B + C + Merge(O, O, O)
                    = P + X + A + Y + B + C + O
                    = PXAYBCO

-                   class D:
                        pass
                    class E:
                        pass
                    class F:
                        pass
                    class B(D, E):
                        pass
                    class C(D, F):
                        pass
                    class A(B, C):
                        pass
                    
                    print(A.mro())
- The algorithm says 
    -       mro(P) = A + Merge(mro(immediate parents) + Parentlist)  
                = A + Merge(mro(B), mro(C), BC)              
                = A + Merge(BDEO, CDFO, BC)
                = A + B + Merge(DEO, CDFO, C)    { D is present in the tail part so leave that list check other list}
                = A + B + Merge(DEO, CDFO, C)
                = A + B + C + Merge(DEO, DFO)
                = A + B + C + D + Merge(EO, FO)
                = A + B + C + D + E + Merge(O, FO)   { O is present in the tail part so leave that list check other list}
                = A + B + C + D + E + Merge(O, FO)
                = A + B + C + D + E + F + Merge(O, O)
                = A + B + C + D + E + F + O
                = ABCDEFO


## Super() 
1. super() allows us to call a method of the parent class from the child class depending on the requirement.
2. it helps in code resuablity without creating a Parent class obj.
3. When a child class has multiple parents and then a super() is called it will follow C3 algo for MRO.
4.              class Person:
                ''' super() demo'''
                    def __init__(self, name, age):
                        self.name = name
                        self.age = age
                    def display(self):
                        print('Name: ', self.name)
                        print('Age: ', self.age)
                
                class Student:
                     def __init__(self, name, age, rollno, marks):
                        super().__init__(name, age)
                        self.rollno = rollno
                        self.marks = marks
                    def display(self):
                        super().display()
                        print('Rollno: ', self.rollno)
                        print('Marks: ', self.marks)

                class Teacher:
                     def __init__(self, name, age, salary, subject):
                        super().__init__(name, age)
                        self.salary = salary
                        self.subject = subject
                    def display(self):
                        super().display()
                        print('Salary: ', self.salary)
                        print('Subject: ', self.subject)

                std = Student('deepak', 15, 01, 59)
                teacher = Teacher('Akshay', 25, 10000, 'History')
                std.display()
                teacher.display()

### How to call a particular  Parent class method using super()
To by pass the method of own parent class and to call a particular Parent class method
1. **parentClassName.methodName(self)**
    -           class A:
                    def m1(self):
                        print('class A method')
                class B(A):
                    def m1(self):
                        print('class B method')
                class C(B):
                    def m1(self):
                        print('class C method')
                class D(C):
                    def m1(self):
                        print('class D method')
                class E(D):
                    def m1(self):
                        B.m1(self)          # to call B class m1() method directly
                        print('class E method')
                
                eRef = E()
                eRef.m1()

1. **super(ChildClass, self).methodName()**
    - If you want to call parent class method then first arg should be the child class of the parent class whose method you want to call, ie. means super od the class which is the 1st arg.
    -           class A:
                    def m1(self):
                        print('class A method')
                class B(A):
                    def m1(self):
                        print('class B method')
                class C(B):
                    def m1(self):
                        print('class C method')
                class D(C):
                    def m1(self):
                        print('class D method')
                class E(D):
                    def m1(self):
                        super(D, self).m1()          # to call C class m1() method directly 
                        print('class E method')
                
                eRef = E()
                eRef.m1()

                
## Case Study for Super()
1. From child class by using super() we cannot call Parent class instance var . We should use self only.
2. From child class by using super() we can call Parent class static var
    -           class Parent:
                    a=10
                    def __init__(self):
                        self.b = 20

                class Child(Parent):
                    def m1(self):
                        print(super().a)      # valid   (to call parent class static var)
                        print(super().b)      # invalid (cannot use super to call Parent class instance var)
                        print(self.b)         # valid   (to call Parent class instance var)

                child = Child()
                child.m1()
3. From **child class constructor by using super() We can call Parent class constructor, instance method, class method and static method**
    -           class parent:
                    def __init__(self):
                        print('Parent constructor')
                    def m1(self):
                        print('Parent Instance method') 
                    @classmethod
                    def m2(cls):
                        print('Parent Class method')
                    @staticmethod 
                    def m3():
                        print('Parent Static method') 

                class Child(Parent):
                    def _init__(self):
                        super().__init__()      => valid
                        super().m1()            => valid
                        super().m2()            => valid
                        super().m3()            => valid
                
                child = Child()
4. From **child class instance by using super() We can call Parent class constructor, instance method, class method and static method**
    -           class parent:
                    def __init__(self):
                        print('Parent constructor')
                    def m1(self):
                        print('Parent Instance method') 
                    @classmethod
                    def m2(cls):
                        print('Parent Class method')
                    @staticmethod 
                    def m3():
                        print('Parent Static method') 

                class Child(Parent):
                    def method1(self):
                        super().__init__()      => valid
                        super().m1()            => valid
                        super().m2()            => valid
                        super().m3()            => valid
                
                child = Child()
                child.method1()


--------------- need to check------------------------
5. From **child class method by using super() We can call Parent class constructor, instance method, class method and static method**
6. From **child class static method by using super() We can call Parent class constructor, instance method, class method and static method**



