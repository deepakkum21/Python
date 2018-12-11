## Features of Python
01. Simple and Easy to learn
02. Freeware and open source
03. High level programming language
04. Platform Independent
05. Portability
06. Dynamically Typed
07. Both Procedure oriented and OOP (does not support method overloading but support operator overloading) i.e not fully OOP
08. Interpreted
09. Extensible
10. Embedded
11. Extensive support of libraries

## Flavours of Python
01. CPython -> C (CPythonVM)
    - This is the most widely accepted implementation of Python. 
    - It is written in the language C, and is an interpreter.
02. Jython or Jpython -> Java (JVM)
    - Jython is a Python implementation written in Java. 
    - A Jython program can import any Java class. 
    - It compiles to Java bytecode.
03. IronPython -> C# (CLR) 
    - IronPython is implemented in C#. 
    - It can function as an extensibility layer to application frameworks written in a .NET language.
04. PyPy(python for speed) -> Jit compiler inside PVM  
    - It is interesting to know that PyPy is Python implemented in Python. 
    - This makes it faster and easier to experiment with. 
    - However, the standard implementation is CPython.
05. RubyPython -> Ruby (Ruby VM)  
    - It acts as a bridge between the Python and Ruby interpreters. 
    - It marshals data between Python and Ruby virtual machines.
06. AnacondaPython -> Large volume of Data
07. StacklessPython -. Python for concurrency
08. Brython -> javascript (javascript interpreter(v8)
    - Brython stands for Browser Python. 
    - It is an implementation of Python that runs in the browser.

## Versions of Python
1. **Python 1.0 - January 1994**
    - Python 1.5 - December 31, 1997
    - Python 1.6 - September 5, 2000
2. **Python 2.0 - October 16, 2000**
    - Python 2.1 - April 17, 2001
    - Python 2.2 - December 21, 2001
    - Python 2.3 - July 29, 2003
    - Python 2.4 - November 30, 2004
    - Python 2.5 - September 19, 2006
    - Python 2.6 - October 1, 2008
    - Python 2.7 - July 3, 2010
3. **Python 3.0 - December 3, 2008**
    - Python 3.1 - June 27, 2009
    - Python 3.2 - February 20, 2011
    - Python 3.3 - September 29, 2012
    - Python 3.4 - March 16, 2014
    - Python 3.5 - May 30, 2014

## Difference between Python 2 and Python 3:
![diffrence](https://github.com/deepakkum21/Python/blob/master/PythonCore/images/python-2-vs-3-2018.png)        
learn python 3 because from **2020 no support for python 2 will be there**

## Python Identifiers
1. A Python identifier is a **name used to identify** a *variable, function, class, module or other object*. 
2. An identifier **starts with a letter A to Z or a to z or an underscore (_)** followed by zero or more letters, underscores and digits (0 to 9).
3. Python **does not allow punctuation characters** such as @, $, and % within identifiers.
4. Python is a **case sensitive programming language**. Thus, **Manpower and manpower are two different identifiers** in Python.
5. An Identifier **should not start with digit** 
    - eg 12Name -> not valid python identifier.
6. **No length restriction but not recomended** to have to lengthy identifier name so that readiblity is maintained.
7. reserved words should not be used as identifiers.
    - if=20 is not allowed and will get invalid syntac error

### Naming conventions for Python identifiers −
1. Class names start with an uppercase letter. 
    - ClassName
2. All other identifiers start with a lowercase letter.
    - methodName
3. Starting an identifier with a **single leading underscore indicates that the identifier is private**. 
    - eg _privateIndetifier
4. Starting an identifier with **two leading underscores indicates a strongly private identifier**.
    - eg __stronglyPrivateIndetifier
5. If the identifier **also ends with two trailing underscores**, the identifier is a **language-defined special name**.
    - eg __languageDefinedIdentifier__

## Reserved Words:
1. The keyword which we cannot use them as constant or variable or any other identifier names. 
2. They have predefined meaning and function.
3. all 33 keywords have alphabet only.
4. Except None, True, flase all have lower case alphabet.    

![Python ReserveWord](https://github.com/deepakkum21/Python/blob/master/PythonCore/images/Python%20reserve%20word%20list.PNG)     

more info:-(https://github.com/deepakkum21/Python/blob/master/PythonCore/pythonReserveWord.md)    

## Python DataTypes:
more info:-(https://realpython.com/python-data-types/)                       

| **datatypes** | **mutable/immutable** | **fundamental data-type** |                       
| ------------- | --------------------- | ------------------------- |               
| int           | immutable             |              yes          |                
| float         | immutable             |              yes          |                
| str           | immutable             |              yes          |                  
| bool          | immutable             |              yes          |                     
| complex       | immutable             |              yes          |                    
| bytes         | immutable             |              no           |                    
| bytearray     | mutable               |              no           |                     
| list          | mutable               |              no           |                         
| range         | immutable             |              no           |                       
| set           | mutable               |              no           |                   
| tuple         | immutable             |              no           |                       
| dict          | mutable               |              no           |                        
| frozenset     | immutable             |              no           |                       
| None          |                       |              no           |                        


### int :-
- To represent integral values (whole no)
- No range , it can accept any whole no 
    - eg x = 364676646549756436976463564343543 (valid)
    - x = -25787453487534537351474843453857 (valid)      >> type(x) => <class 'int'>
- Integral values can be represnt using 4 forms:-
    - Decimal form
    - Binary form
    - Octal form
    - Hexa Decimal Form
1. Decimal Form (Base-10)
    - Allowed digit (0-9)
    - it is default form of representation

2. Binary Form (base-2)
    - Allowed digit (0,1)
    - 0B or 0b should be prefixed to represent   binary form
    - only allowed for intergal no and not for floating point
    - eg 0B1111 , 0b011011

3. Octal Form (base-8)
    - Allowed digit (0-7)
    - 0O or 0o should be prefixed to represent   Octal form
    - only allowed for intergal no and not for floating point
    - 0O014526,  0o74123470

4. HexaDecimal Form (base-16)
    - Allowed digit (0-9,A-f)
    - 0x or 0X should be prefixed to represent   HexaDecimal form
    - only allowed for intergal no and not for floating point
    - eg 0X458435434ABF, 0x24babf

#### Base Conversions
- To convert to any of the above form use
    - bin(x)
    - oct(x)
    - hex(x)
    note :- x can be any thing decimal, octal, binary, hexadecimal

### float :-
1. To represent  number with floating point.
2. no range 
    - eg x = 354331.545643    >> type(x)  => <class 'float'>
3. exponential form is allowed
    - eg x = 12.456e3   => 12.456*1000 = 12456
4. Floating point no should be represented using decimal form no and not using octal, binary, hexadecimal
    - e.g x = 0B011.01 (invalid)
    - e.g x = 0o01745.0153 (invalid)
    - e.g x = 0X011.018765a (invalid)


### complex :-
1. Complex numbers are specified as <real part>+<imaginary part>j.
2. Can't use anything inplace of j in the imaginary part.
    - eg.  x=2+3j   >>>  type(2+3j)   => <class 'complex'>
3. - x = 3+5j   (valid)
   - x = 5j+3   (valid) 
4. Real part can be specified using Decimal, Binary, Octal, HexaDecimal but imginary part should be specified only using Decimal(int or float)
    - eg 12+5j       (Valid)
    - eg 0b1101+5j   (Valid)
    - eg 0o12451+5j  (Valid)
    - eg 0X45A12+5j  (Valid)
    - eg 12+0B11j    (inValid)
    - eg 12+0o5j     (inValid)
    - eg 12+0XA5j    (inValid)
5. All mathematical operation except % (modulo) can be applied
    - eg A=(5+4j), B=(7+3j) , A+B      (valid)
    - eg A=(5+4j), B=(7+3j) , A-B      (valid)
    - eg A=(5+4j), B=(7+3j) , A*B      (valid)
    - eg A=(5+4j), B=(7+3j) , A/B      (valid)
    - eg A=(5+4j), B=(7+3j) , A%B      (invalid)
6. .real and .imag are the  predefined variable to get the real and imaginary part from the complex no.
    - eg A = 4+6j   , c.real => 4.0 , c.imag => 6.0
7. Internally the complex no is maintained as floating no
    - eg. X = 40+5j  => (40+5j) but when you will try to get real and imag no using .real and .imag then it is represented as floating no.


### bool :-
1. To represent Truthiness.
2. True and False are the value for bool (both start with capital letter)
3. Internally python store int value for both
    - eg True  => 1
    - eg False => 0
4. True + True   => 1 + 1 => 2
5. True + False  => 1 + 0 => 1
6. True - True   => 1 - 1 => 0
7. False - True  => 0 - 1 => -1

### str: -
1. To represent any sequence of characters.
2. There is nothing like char datatype everything is string if it is surrounded by '',"",'''''' (single,double,triple quotes).
3. Trple quotes:- '''string''':
    - To define multiple string literals.
    - To use ' and " as symbols.
4. Recomended to use '' single quotes as string , python also uses '' to represnt string.
5. Python supports both +ve and -ve indexes.
    -  +ve : forward direction
    -  -ve : backward direction
    - eg: S = 'Deepak'  =>  S[0]   => 'D'   =>  S[-1]  => 'k'


### bytes: -
1. To represent a group of byte values.
2. only allowed values are 0 to 255.
    - x = [10,20,30] => b = bytes(x)  => type(b)  <class 'bytes'>
3. Cannot change the value of byte
    - x = [10,20,30] => b = bytes(x)  => b[0] => 10 =. b[0] = 50 (invalid)
4. if want to store binary data of img, audio, video files
5. it is **immutable**.


### bytearray: -
1. It is same as bytes except we can change the value.
2. To represent a group of byte values.
3. only allowed values are 0 to 255.
    - x = [10,20,30] => b = bytearray(x)  => type(b)  <class 'bytearray'>
4. Allowed to change the value of bytearray
    - x = [10,20,30] => b = bytearray(x)  => b[0] => 10 =. b[0] = 50 (valid)
5. It is **mutable**

### list[]: - 
1. To represent group of individual object.
2. Insertion order is preserved.
3. Duplicate object are allowed.
4. Hetrogeneous objects are allowed.
5. It is **mutable** 
6. It is dynamic :-
    - .append() -> to increase the size
    - .remove() -> to decrease the size

### tuple(): -
1. To represent group of individual object.
2. Insertion order is preserved.
3. Duplicate object are allowed.
4. Hetrogeneous objects are allowed.
5. It is **immutable** 
6. Read only version of List.
7. Cannot increase or decrease the size , i.e. it is not dynamic
8. To create 1 length tuple 
    - eg t = **(10,) => type(t) => <class 'tuple'>**
    - if t = (10) => type(t) =. <class 'int'>
9. **() is optional**
    - eg t = 10,30,4,56  => type(t) => <class 'tuple'>
 
### set{}: -
1. To represent group of individual object where order is not important.
2. Insertion order is **not** preserved.
3. Duplicate object are not allowed.
4. if duplicate object are present would eliminate itself by storing unique one.
5. it doesnot support indexing , slicing
    - eg s = {10,20,30}   => s[0]   => invalid
6. It is **mutable** 
7. It is dynamic :-
    - .add() -> to increase the size
    - .remove() -> to decrease the size 
8. use loop to get the data 
    - for x in s : print(x)
9. s = {} is dict not set
10. To create empty set 
    **emptySet = set()**    

### frozenset: -
1. same as set
2. it is **immutable**
3. it is not dynamic i.e cannot add or remove object 
4. s = {10,20,30}   => fs = frozrnset(s)   => type(fs)  => <class 'frozenset'>

### dict{}:-
1. To represent group of individual object as key-value pairs.
2. Key :
    - duplicates are not allowed.
    - hetrogenous object is allowed
    - key **can be tuple but not list**
3. Value :
    - duplicates are allowed.
    - hetrogenous object is allowed
4. To add key-value in existing dict
    eg: p = {101:'deepak'}   =>  p[key] = value  => p[102] = 'abc'   => p  => {101:'deepak', 102:'abc'}
5. it is **mutable**
6. if trying to add duplicate key but value is different , wouldn't give erroe but it will override the previous value with the new value for that key which was duplicate.

### range: -
1. To represent sequence of numbers.
2. It is **immutable**.
3. Form1 : **range(x)**
    - from 0 to x-1 
    - eg r= range(10)    =>  for i in r: print(i)    => 0,1,2,3,4,5,6,7,8,9
4. Form2 : **range(x, y)**
    - from x to y-1
    - eg r= range(4,10)    =>  for i in r: print(i)    => 4,5,6,7,8,9
5. Form3: **range(begin, end, step)**
    - from begin to end-1 with next increment step
    - eg r= range(4,10,3)    =>  for i in r: print(i)    => 4,7





## Slice Operator :-
- The slice operator [n:m] returns the part of the string from the n’th character to the m’th character, including the first but excluding the last. 
- In other words, start with the character at index n and go up to but do not include the character at index m. 
- If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string.
- There is **no Index Out Of Range exception for a slice**. A slice is forgiving and shifts any offending index to something legal.
- Two forms of sclice
1. [startindex : end-1index]
    - s[:4] => returns value at index 0,1,2,3
    - s[:] => returns value from start to end index
    - s[1:] => returns value from index 1 to last index
    - if s has index till 5 and s[1:100] => returns value from index 1 to last if end index is greater than the total index of string, no outof range exception is raised
    - s[-1:-3] is valid
    
2. [startindex : end-1index : step]
    - default step value is 1
    - step: is the no of character to skip
    - s[2:5:2] => skips one character starting from 2 and returns value for index 2,4
    - s[-1,-5,-1] => starts from -1 index and goes one step backward and returns value for -1,-2,-3,-4
    - s[::-1] => reverses the string

## Type Casting/ Type Coersion
- int()
- float()
- bool()
- str()
- complex()

1. **int(x)**
    - int(float): int(123.456) => 123
    - int(complex) : int(10+5j) => invalid complex to int not allowed  
    - int(bool) : int(True) => 1  (0 : for False)
    - int(string) : int("10") => valid 10 (string should be valid decimal integral)
    - int(string) : int("0B10") => invalid
    - int(string) : int("0o10") => invalid
    - int(string) : int("0X10") => invalid
    - int(string) : int("10.5") => invalid : not integral
    - we can convert any type to int except complex
    - we can convert str to int if and only if str is integral literal of base10

2. **float(x)**
    - we can convert any type to float except complex
    - we can convert str to float if and only if str is integral literal or floating point literal of base10 
    - float(float): float(123) => 123.0
    - float(complex) : float(10+5j) => invalid complex to float not allowed  
    - float(bool) : float(True) => 1.0  (0.0 : for False)
    - float(string) : float("10") => valid 10.0 (string should be valid decimal integral)
    - float(string) : float("0B10") => invalid
    - float(string) : float("0o10") => invalid
    - float(string) : float("0X10") => invalid
    - float(string) : float("10.5") => valid 

3. (a).  **complex(x)**
    - here x is the real part and imaginary part is not specified therefore, is 0.                                                          
    ![example](https://github.com/deepakkum21/Python/blob/master/PythonCore/images/complex()example.PNG)
3. (b). **complex(x,y)**
    - here x is the real part and y is the imaginary part.
    - complex(string, string) : complex("10", 4.5) => invalid (cannot take second arg when 1st arg is String)
    - complex(int/float, string) : complex(10, "4.5") => invalid second arg cannot be string
    - complex(float, float) : complex(10.5, 4.5) : valid => 10.5+4.5j

 4. **bool(x)**
    - *when x is int*
        - if x is 0 then False    
        - if x is other than 0 i.e. -ve or +ve it is True
    - *when x is floating point*
        - if x is 0.0 or equal the it is False
        - if x is non zero i.e. 0.01, -0.002 then it is True
    - *when x is complex*
        - when real and imaginary both part is 0 then False . eg bool(0.0 + 0.0j)  => False   , bool(0j) => False
        - when any one or both value is non zero then it is True
    - *when x is string*
        - empty string is False  e.g.: bool('')  => False
        - non empty string is always True

5. **str(x)**
    - anything can be converted to string

## Fundamental datatypes VS immutability
1. All fundamental data types are immutable (once object is created not allowed to change its content, if changed with those changes a new object will be created).
2. Immutablity helps in reusability (it varies from flavour to flavour of python) use **id()** to check the address:        

| **Data type** | **Reusability** | **What extent** |                   
| ------------- | --------------- | --------------- |                   
| int           |  yes            | 0 to 256       |               
| float         |  no             | n.a.       |                  
| bool          |  yes            | always       |            
| str           |  yes            | varies from flavour to flavour |              
| complex       |  no             | n.a.        |              


