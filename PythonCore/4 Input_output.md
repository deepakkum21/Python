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
        - locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.
        - eg : eval('10 + 20 + 30') => 60  

### Reading multiple values from keyword in a single line:-
1. input('Enter 2 no: ').split() 
    - **split()** will split the entered value w.r.t space . eg: if '2 8' entered then split() will make it ['2', '8']
    - a,b = [int(x) for x in input('Enter 2 no: ').split()]
    - the above statement will first take input as string with a space if entered ('2 3') then this will be converted to string list by spliting from space using split() (['2','3']) then for each x it will bw converted to int (2,3) but **assign multiple values it has to be converted to list or tuple** and that is being done after this a will be assigned first value and b the other.
2. input('Enter 2 no: ').split(',') 
    - **split(',')** will split the entered string value w.r.t. ',' eg: if '2,8,9' entered then split(',') will make it ['2', '8', '9']

## Command Line Argument:-
1. sys => name of module
2. argv => list name in the sys module
3. the first value at index 0 is filename.py 
    - i.e. test.py 10 20 30 => argv[0] -> test.py => argv[1] -> 10 => argv => ['test.py', '10', '20', '30']
    - all the values are stored in the form of string
4. If want to give argument with space, then 
    - test.py "Deepak kumar" 10 20
        - argv -> ['test.py', 'Deepak kumar', '10', '20']
    - **"" is compulsory if want to enter string having space** single quote('') will be treated as single string and after space will be treated as another string.



## Output statement:-
1. **print(str)**
    - it has 2 attribute
        - end: default value '\n' (eol)
        - sep: default value (space ' ' )
    - print('abc') => vaild
    - print('xyz'+'bcs') => vaild
    - print('vxa'*2) => vaild
    - print(3*'yza') => vaild
    - print('abc'+'abc') => vaild
    - print('abc'+3) => invalid (while concatenation all operand should be string)
    - print('abc'*'abc')  => invaild (while  * at least one should be int on the adjacent side of string )
    - print('abc'*10 + 'abc') => valid
    - print('hello','world') => valid (if multiple arg are there separated with , then in o/p => is separated with space( ))
        - **defalut separator is space**
    - print('hello','world',**sep=','**) => valid (hello,world)
    - eg
        - print('deepak')
        - print('kumar') both will be printed in the different line because default value of end is '\n'
        - print('deepak',end=' ')
        - print('kumar') =>  deepak kumar
    - **formatted print**
        - %i ---> int
        - %d ---> int
        - %f ---> float
        - %s ---> string
        - print('formatted string' %(list of variables))
        - eg a,b,c = 10,20,30   => print('a value of %i' %a)  -> a value is 10
        - eg a,b,c = 10,20,30   => print('b value of %i and c value is %d' %(b,c))  -> b value is 20 and c value is 30
    - **print with replacement operator**
        - fisrtName = 'deepak'
        - lastName = 'kumar'
        - **print('{} your last name is {}'.format(firstName, lastName))** => deepak your last name is kumar