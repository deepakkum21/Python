# Input/Output statements

## Reading dynamic input from keyboard
1. raw_input()
2. input()

| **function** | **in Python 2.x** | **in python 3.x** |                                                                                      
| ------------ | ----------------- | ----------------- |                                                                                          
| raw_input()  | takes exactly what the user typed and passes it back as a string. e.g x=raw_input('a: ') => a: 5 => type(x) => <class 'str'> | was **renamed to input()** so now *input() returns the exact string*. e.g x=raw_input('a: ') => a: 5 => type(x) => <class 'str'>|
| input()      | first takes the raw_input() and then internally performs an **eval()** on it as well. e.g x=input('a: ') => a: 5 => type(x) => <class 'int'> | input() was removed. can be achieved old functionality by manually performing eval(input()) . e.g x=eval(input('a: ')) => a: 5 => type(x) => <class 'int'> |    

**eval()** :- method runs the python code (which is passed as an argument) within the program.
- The eval() takes three parameters:
    - **eval(expression, globals=None, locals=None)**
    - expression - this string as parsed and evaluated as a Python expression
    - globals (optional) - a dictionary
    - Alocals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.