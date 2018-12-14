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
- 
