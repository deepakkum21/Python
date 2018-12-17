# Modules
1. Modules refer to a file containing Python statements and definitions (functions and variables saved to a file).
2. it helps in code resuability .
3. A file containing Python code, for e.g.: **example.py, is called a module and its module name would be example**.
4. define our most used functions in a module and import it, instead of copying their definitions into different programs.

## Module creation;-
1. Let us create a module. Type the following and save it as example.py.
2. *Python Module example*
    -        def add(a, b):
    -           """This program adds two
    -           numbers and return the result"""
    -           result = a + b
    -           return result

## How to import modules 
1. **if imported whole module**
    - *import module*  or *import module as alias-module-name*
    - then (.) operator is used to call a function that is defined in the imported module prefixed with module name
    - example.add(4.5,8)  or alias-module-name.function-name(parameters)
2. **if imported a particular function**
    - *from module-name import module-function-name*   or *from module-name import module-function-name1  as function-alias-name*  
    - then no need to use (.) operator and module-name, straight away function can be used with passing parameters into it.
    - *module-function-name(parameters)*  or *function-alias-name(parameters)*
3. **import all names**
    - **from module-name import *** , then also no need to use module name to call any function defined in that particular module as all functions mentioned in the are imported.

## Python Module Search Path
1. While importing a module, Python looks at several places. 
2. Interpreter **first looks for a built-in module** then **(if not found) into a list of directories defined in sys.path**. The search is in this following order:-
    - The current directory.
    - PYTHONPATH (an environment variable with a list of directory).
    - The installation-dependent default directory.

## Reloading a Module
1. For every module .PYC file will be generated which is the compile form of .py file.
2. These .pyc file are stored in the **__ pycache__**
3. The Python interpreter imports a module only once during a session
4. In python it doesn't matter how many times a module is being loaded or imported, a module will be imported i.e loaded only one time.
5. The feature of module getting loaded only once irrespective of no. of times module is being loaded, 
    - has advantage:-
        code execution is fast as it ha to load only once
    - has disadvantage also
        - once loaded, if it is modified updated version is not available
        - **sol-**  by using **reload() of imp module** 
        - eg :    reload(module-name)


## Finding members of a module
1. **dir(module-name)** is used to find all the members of the module
2. dir()    => list of members of a current module
3. dir(module-name)    => list of members of a module-name module
4. some of the default members present in every module are:-
    - '__ builtins__','__ cached__','__ doc__','__ file__','__ initializing__','__ loader__','__ name__','__ package__',
5. the __ name__ attribute contains **the name of the module**.


## help for any module
1. **help(module-name)** to get help for any module
2. this will give list of methods present in the module


## Random module
1. this module has function called random() 
    - which generates a **random float no from 0 to 1 (not inclusive 0<x<1**
2. **randint(from, to)**
    - it is going to generate random value from(1st arg) to (2nd arg) 
    - it will return a no 1<=x<=100
3. **uniform(from, to)**
    - it is going to generate random float value from(1st arg) to (2nd arg) 
    - it will return a random float value (1<x<100 ) (1 and 100 are exclusive)
4. **randrange(from, to, step)**
    - default values:-
        - from:- 1
        - step:- 1
    - from value = from-1
    - it returns a random int
5. **choice(sequence)**
    - sequence is a mandatory parameter that can be a list, tuple, or string.
    - choice(sequence) returns a random object. 
