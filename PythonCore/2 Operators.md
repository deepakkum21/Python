# Python Operators
- Arithmetic operators
- Relational operators / comparison operators
- Logical operators
- Bitwise operators
- Assignment operators
- Special operators

## Arithmetic operators: -                                                                            
| **Operator** |	**Description** |	**Example** |                                                         
| ------------ | ------------------ | ------------- |                                  
| + - Addition | 	Adds values on either side of the operator. |	a + b = 30 |                                                                
| - - Subtraction |	Subtracts right hand operand from left hand operand. |	a – b = -10 |                                                                
| * - Multiplication |	Multiplies values on either side of the operator |	a * b = 200 |                                                                
| / - Division |	Divides left hand operand by right hand operand. Always return result in floating point |	b / a = 2.0 , 5.0/2.0 = 2.5 |                                                                
| % - Modulus |	Divides left hand operand by right hand operand and returns remainder |	b % a = 0 |                                                                
| ** - Exponent |	Performs exponential (power) calculation on operators |	a**b =10 to the power 20 |                                                                
| // -	Floor Division |  The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) . if any of the argument is floating point, the result is in floating point and if both are int the reult is of int type | −	9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0 , 3//2.0 = 1.0 , 3.0//2.0 = 1.0 , 3.0//2 = 1.0 |      

1. +, * can also be applied to string: -
    - (+) operator acts as concatenation for string
        - 'deepak'+'kumar'  => deepakkumar
        - **but all arg should be string**
        - 'deepak'+True => invalid
        - 'deepak+10 => invalid
    - (*) string repetition operator
        - 'deepak'*3 => deepakdeepakdeepak
        - 3*'deepak' => deepakdeepakdeepak
        - in this at least one should be int other as string
2. divison by zero                                  

| **operation** | **result in Java**       | **result in python** |                  
| ------------- | ------------------------ | -------------------- |
| 10/0          | divide by zero exception | ZeroDivisonError     |
| 0/0           | divide by zero exception | ZeroDivisonError     |
| 0.0/0, 1.0/0  | infinity                 | ZeroDivisonError     |
| 0.0/0.0       | NaN (not a number)       | ZeroDivisonError     |

## Relational operators / comparison operators           

| **Operator** |	**Description** |	**Example** |                                                     
| ------------ | ------------------ | ------------- |                                        
| == |	If the values of two operands are equal, then the condition becomes true. |	(a == b) is not true. |
| != |	If values of two operands are not equal, then condition becomes true. |	(a != b) is true. |
| <> |	If values of two operands are not equal, then condition becomes true. |	(a <> b) is true. This is similar to != operator. |
| > |	If the value of left operand is greater than the value of right operand, then condition becomes true. |	(a > b) is not true. |
| < |	If the value of left operand is less than the value of right operand, then condition becomes true. |	(a < b) is true. |
| >= |	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. |	(a >= b) is not true. |
| <= |	If the value of left operand is less than or equal to the value of right operand, then condition becomes true. |	(a <= b) is true. |   

1. Relational operators can also be used with string
    - it consider the unicode and performs logical operation
    - eg 'a'<'b' => True (97<98)
    - 10 < 'deepak' => invalid
2. Relational operators can be applied with bool
    - True > False => True (1 > 0)
    - 10 < False => False valid
3. chaining of relational operator possible
    - **True if all is True**
        - eg 10<20<30<40 => True
        - 10>5>1>0 => False
    - **False if any one comparision is False**
        - eg 5>2>1>8 => False
4. Equality operators (==, !=)
    - it is applicable for incomparable types also
    - == meant for content comparision
    - 10 == 'deepak' => Flase
    - True == True => True
    - chaining of equality operator is also possible
        - **True if all is True**
            - 10 == 10 == 10 => True
        - **False if any one equality is False**
            - eg 10 == 10 == 20 => False  

## Logical Operator: -
1. For bool type:- 

| **Operator** |	**Description** |	**Example** |                                           
| ------------ | ------------------ | ------------- |
| and Logical AND |	If both the operands are true then condition becomes true. | (True and True) is True, (True and False) is False |
| or Logical OR |	If any of the two operands are non-zero then condition becomes true. |	 (True or False) is True, (False and False) is False |
| not Logical NOT |	Used to reverse the logical state of its operand. |	 not(True) => False |

2. For non bool type:
    - 0 -> False
    - non zero -> True
    - '' (empty string) -> False
    - string (except '' empty string) -> True
    - None -> False
    - **x and y => if x is True, then ans is y**
        - eg 10 and 20 => 20
        - 45 and 0 => 0
        - True and 4 => 4
        - 'k' and 'kj' => 'kj'
        - 'k' and '' => ''
        - 'l' and None => None
    - **x and y => if x is False, then ans is x**
        - eg 0 and 20 => 0
        - 0 and 0 => 0
        - False and 47 => False
        - '' and 'y' => ''
        - None and 'l' => None
    - **x or y => if x is True, then ans is x**
        - eg 10 and 20 => 10
        - 45 and 0 => 40
        - True and 4 => True
        - 'k' and 'kj' => 'k'
        - 'k' and '' => 'k'
        - 1 or None => 1
    - **x or y => if x is False, then ans is y**
        - eg 0 and 20 => 20
        - 0 and 0 => 0
        - False and 47 => 47
        - '' and 'y' => 'y'
        - None or 'l' => 'l'
    - Not
        - not '' => True
        - not None => True
        - not 0 => True
        - not 45 => False
        - not 'kl' => False
        - not ' ' => False
    
## Bitwise Operators: 
1. Bitwise operator works on bits and performs bit by bit operation.
2. Can be **only applied for Int and bool** types not for string type.
3. & => **if both bits are 1 then result is 1**
4. | => **if at least one bit is one then result is 1**
5. ^ => **if both bits are different then result is 1**
6. **~ (bitwise complement operator)** :-
    - The most significant bit is sign bit
    - 0 means +ve no.
    - 1 means -ve no.
    - +ve no will be directly represented in the memory.
    - -ve no will be indirectly represented in the memory.
        - by using 2's complement.
    - 2's complement => first find 1's complement (interchanging 0 and 1) and then add 1.
    - eg ~5 => -6
        - in memory 5 is represented in 32 bit (00000000000000000000000000000101) => here 0 in MSB means +ve
        - now we have to find complement means inverse so place 0 in place of 1 and vice versa
        - now it will become 11111111111111111111111111111010 , here 1 in MSB means -ve no.
        - since it is -ve no it has to be represented in the 2's complement form.
        - (11111111111111111111111111111010) in 2's complement
            - 1's complement of (11111111111111111111111111111010) => (100000000000000000000000000000101)
            - now add 1 to (100000000000000000000000000000101) to get 2's complement => (100000000000000000000000000000101) + 1 => (100000000000000000000000000000110)
            - since 1 is in MSB => -ve no and 110 =>  6 in total -6
            - ~5 => -6
            - ~-6 => 5
            - ~10 => -11
            - ~-56 => 55
7. **shift (>>,<<) operator**:-
    - Left shift (<<)  (x << y) :-
        - this enables to shift y bits to the left 
        - the vaccant bits to the right side is filled with 0
        - eg 5 << 2
        - (00000000000000000000000000000101) when shifted 2 bit left => (000000000000000000000000000101__)
        - the vacant spaces are filled with 0 => (00000000000000000000000000010100)
    - Right shift (>>)  (x >> y):-
        - this enables to shift y bits to the right 
        - the vaccant bits to the left side is filled with sign bit (i.e. if x is +ve it is filled with 0 , if x is -ve it is filled with 1)
        - eg 5 >> 2
        - (00000000000000000000000000000101) when shifted 2 bit right => (__000000000000000000000000000001)
        - since 5 is +ve the vaccant bits are filled with 0
8. Bitwise operator effect on bool type
    - True & False => False ( & if both bits are 1 then 1) => 1 & 0 => 0 (False)
    - True | False => True ( | if at least one bit is 1 then 1) => 1 | 0 => 1 (True)
    - True ^ Fasle => True ( ^ if both bit are different the 1) => 1 ^ 0 => 1 (True)
    - ~False => -1  ( ~False => ~0 => -1)
    - ~True => -2  ( ~True => ~1 => -2)
    - True>>2 => 0 ( True>>2 => 1>>2 => 0)


## Assignment Operator: -
1. increment (++x, x++) and decrement operator are not allowed in python
2. but (++x), (--x) => vaild (because it treates as (+ (+(x))) same for --x)
3. compound operators like -=, *=, /=, //=, &=, %=, |=, >>=, <<=, **=, ^=


## Special Operators:- 
1. **Identity Operators (is , is not)**
    - **is => (addess/ refrence comparision**
        - == => content comparision
        - x is y => return True if both x and y is pointing to the same object 
        - x==y => return True if both have same content                        

        | **operator** | **in Java**       | **in python** |                                                   
        | ------------ | ------------------------ | -------------------- |                                                                    
        | is(py) / .equals()-java | content comparision | address/ reference comparision     |                                            
        | ==           | address/ reference comparision | content comparision    |                            

    - **is not**
        - complement of is

2. **Membership Operators (in , not in)**
    - **in**
        - x in y => evaluates to True if x is the member of y
    - **not in**
        - complement of in operator
        - x not in y => evaluates to False if x is the member of y

## Ternary oerator imp:
1. **a = b if condition else c**
    - implies a will be equal to b if and only if the condition evaluates to True else a will be equal to c.


## Taking Input from keyboard in Python.
a = input('Enter value for a: ')                                                                                                                    
**input() -> is used to take input from keyboard**
- By default the type of a is string
- if want in int convert it 
    - a = int(input('Enter value for a: ') )
    - eg find minimum among 3 no
    - max = a if a < b and a < c else b if b < c else c   

## Operator Precedence:-

| **Sr.No.** |	**Operator** | **Description** |                                         
| ---------- | ------------- | --------------- |                          
| 1	         | **            | Exponentiation (raise to the power) |
| 2        	 | ~ + -         | Complement, unary plus and minus (method names for the last two are +@ and -@) |
| 3	         | * / % //      | Multiply, divide, modulo and floor division |
| 4	         | + -           | Addition and subtraction |
| 5	         | >> <<         | Right and left bitwise shift |
| 6	         | &             | Bitwise 'AND' |
| 7	         | ^ |           | Bitwise exclusive `OR' and regular `OR' |
| 8	         | <= < > >=     | Comparison operators |
| 9	         | <> == !=      | Equality operators |  
| 10	     | = %= /= //= -= += *= **= | Assignment operators | 
| 11	     | is is not     | Identity operators | 
| 12	     | in not in     | Membership operators |
| 13	     | not or and    | Logical operators |      

