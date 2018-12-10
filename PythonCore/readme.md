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

![Python ReserveWord](https://github.com/deepakkum21/Python/blob/master/PythonCore/images/Python%20reserve%20word%20list.PNG)
more info:-(https://github.com/deepakkum21/Python/blob/master/PythonCore/pythonReserveWord.md)


