# Python Operators
Arithmetic operators
Relational operators / comparison operators
Logical operators
Bitwise operators
Assignment operators
Special operators

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

    