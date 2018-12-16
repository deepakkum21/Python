# Functions
1. In Python, function is a group of related statements that perform a specific task.
2. Functions help break our program into smaller and modular chunks.
3. it avoids repetition and makes code reusable.

## Syntax of Function: -
-        def function_name(parameters):
	        """docstring"""
	        statement(s)
            return # optional

    - Keyword **def** marks the start of function header.
    - A function_name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
    - Parameters (arguments) through which we pass values to a function. They are optional.
    - A colon (:) to mark the end of function header.
    - **Optional documentation string (docstring)** to describe what the function does.
    - One or more valid python statements that make up the function body. Statements must have same indentation level (usually 4 spaces).
    - An **optional return statement** to return a value from the function.

## How to call a function in python?
Once we have defined a function, we can **call it from another function, program or even the Python prompt**. To call a function we simply type the function name with appropriate parameters.

## Docstring :
1. The **first string after the function header** is called the docstring and is short for documentation string. 
2. It is **used to explain in brief, what a function does**.
3. generally use triple quotes so that docstring can extend up to multiple lines.
4. This string is available to us as **__doc__ attribute** of the function.
    - eg **print(functionName.__doc__)**

## The return statement: -
1. The return statement is used to exit a function and go back to the place from where it was called.
2. **return [ expression_list]**
3. This statement can contain expression which gets evaluated and the value is returned. 
4. If there is **no expression in the statement or the return statement itself is not present** inside a function, **then the function will return the None object**.
5. can return multiple values at a time.


## Types of Functions
- built-in functions
- user defined functions

## Types of Parameters :-
- positional
- keyword
- default
- var-arg
- keyword-var agr

1. **positional arg**
- order of arguments is imortant
- no of arg passed thrugh function calling should match no of parameters of function defined.
-           def sumOfNo(num1, num2, num3):
-               sum = num1+num2+num3
-               return sum
-           sumOfNo(5, 6, 8)

2. **keyword arg**
- order of arguments is not imortant
- no of arg passed thrugh function calling should match no of parameters of function defined.
- can mix positional with keyword arg but **positional arg should be first the keyword agv**
-           def sumOfNo(num1, num2, num3):
-               sum = num1+num2+num3
-               return sum
-           sumOfNo(num2=5, num1=6, num3=8)    => keyword arg eg
-           sumOfNo(num2=5, 6, 8)       => invalid
-           sumOfNo(5, 6, num3=8)       => valid
-           sumOfNo(5, num2=6, num3=8)  => valid
-           sumOfNo(5, num1=6, 8)       => invalid  (num2 got multiple values)

3. **default arg**
- default arg should be placed in the last, i.e. after all non-default arg
-            def sumOfNo(num1, num2=10, num3): pass   => invalid
-            def sumOfNo(num1, num2, num3=15): pass   => valid

4. **var-arg**
- when we have to pass any no of arg (zero - any)
- * is prefixed with the argname  function_name(*argName)
- internally the *arg is tuple.
- if var-arg parameter is given first and then positional arg then , compulsory positional arg has to be called using keyword arg
-           def varArgFunction(*arg, name): pass
-           varArgFunction(1,2,3,4, name='deepak')    => vaild
-           varArgFunction('deepak' ,1,2,3,4)    => invaild   (gets confused which parameter is for what)
-           def varArgFunction(*arg): pass
-           varArgFunction(1,2,3,4)        => valid  
-           varArgFunction()               => valid
-           varArgFunction (7)             => valid
-           varArgFunction (7,6)           => valid

5. **Keyword-var-arg**
- When want to pass argument as key and value fun_name(name='deepak', city='chennai') and want name and city to be treated as key and associated value as value for the key.
- **should be prefixed with the arg => func_name( **keyvararg)
-           def keyVarArg(**arg): pass
-           keyVarArg(name='deepak', city='chennai') 


## Recurcive Function
- Recursion is the process of defining something in terms of itself.
    - **real worl eg** =>  two parallel mirrors facing each other. Any object in between them would be reflected recursively.
- Function calling itself 
    - find the factorial of an integer.
- Every recursive function **must have a base condition that stops the recursion** or else the function calls itself infinitely.
- **Advantages of Recursion**
    - Recursive functions make the code look clean and elegant.
    - A complex task can be broken down into simpler sub-problems using recursion.
    - Sequence generation is easier with recursion than using some nested iteration.
- **Disadvantages of Recursion**
    - Sometimes the logic behind recursion is hard to follow through.
    - Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
    - Recursive functions are hard to debug.


## Anonymous function/ lambda function
1. function that is defined without a name.
2. normal functions are defined using the def keyword, in Python **anonymous functions are defined using the lambda keyword**.
3. **use** => instant or one-time usage purpose , anonymous or lambda function is created
4. syntax   **lambda arguments: expression**
5. **Use of Lambda Function in python**
    - generally it is used **as an argument to a higher-order function** (a function that takes in other functions as arguments). Lambda functions are **used along with built-in functions like filter(), map(), reduce()** etc.
    - filter() function in Python takes in a function and a list as arguments, return filter type object.
        - **new_list = list(filter(lambda x: (x%2 == 0) , my_list))**
    - map() function in Python takes in a function and a list, return map type object..
    - returns same no of elements as the no of the lements were in the list which was passed as arg.
        - **new_list = list(map(lambda x: x * 2 , my_list))**

## Nested Function:
- When the functionality is required within the function.
-       def outer():
-               def inner(a,b):
-                   return a+b
-               inner(5,10)
-               inner(4,9)
- A function can return function 
-       def outer():
-               def inner(a,b):
-                   return a+b
-               inner(5,10)
-               return inner      // returning a function
- A function can take function as arg
    - filter(lambda function , argList), map(lambda function , argList)
- **if want to xecute inner() then the outer function must reurn inner()**
- f= functionname()  -> calling function with functionname
- f= functionname    -> giving alias to the function with functionname 


## higher order functions
1. Function that take other functions as arguments
        def inc(x):
            return x + 1

        def dec(x):
            return x - 1

        def operate(func, x):
            result = func(x)
            return result
        operate(inc,3)
        operate(dec,3)

## Function Decorator
1. A decorator takes in a function, adds some functionality and returns it.
2. **add functionality to an existing code**
3. It help us to make our code shorter and more pythonic.
4. **@deco-function-name is added as the anotation whose decorator is created with deco-function-name
    - eg
    -           def decofunction(func):
    -                def innerfun(name):
    -                   if(name='deepak'):
    -                       print('Deepak name got')
    -                   else:
    -                       func(name)
    -               return innerfunc
    -           @decofunction
    -           def functobedecorated(name):
    -               print('deepak name was not there')
    -           functobedecorated('abc')
    -           functobedecorated('deepak')
5. When @deco-function-name is used as a anotation for any function then automatically decorator function is clled on be half of it.
6. When want to call manually
    - then **decorRef = deco-function-name(functobedecorated)**
    - decorRef will now hold decofunction as alias
7. **Chaining Decorators in Python**
- function can be decorated multiple times with different (or same) decorators. 
-                def star(func):
-                   def inner(*args, **kwargs):
-                       print("*" * 30)
-                       func(*args, **kwargs)
-                       print("*" * 30)
-                   return inner
- 
-                def percent(func):
-                   def inner(*args, **kwargs):
-                       print("%" * 30)
-                       func(*args, **kwargs)
-                       print("%" * 30)
-                   return inner
- 
-               @star
-               @percent
-               def printer(msg):
-                   print(msg)
-               printer("Hello")    
