# Flow Control
These decide the order in which the statement will be executed
1. Selection statement (if,elif,if else)
2. Iterartive statement (for, while )
3. Transfer statement (pass, continue, break)                          



1. **Selection Statement**
- when decision is made on some criteria.
    - **if** 
        - When it reaches an if statement, the computer only executes the body of the statement only if the condition is true.
    - **if condition: body  else : body**
        - if block is executed when condition evalutes to true otherwise else body is executed
    - **if condition: body elif condition : body  else : body**

2. **Iterative Statements**
- When want to execute a group of statement multiple times
    - **for loop**
        - for x in range(), list, tuple , string : do some action 
    - **while condition**
        - as long as the condition is true
        - when donot know the no of iteration in advance
        -  while condition : body

3. **Transfer Statement**
- When want to tranfer the control from one statement to other
    - **break**
        - based on some sondition when want to break the loop execution
        -     for i in range(10) : 
        -       if(i==6):
        -           break
        -       print(i,end=' ')
        - o/p =>0 1 2 3 4 5
    - **continue**
        - to skip current iteration and continue with next iteration for that particular loop in which it was declared
        - it doesnot transfer the control to end loop
        -     for i in range(10) : 
        -       if(i==6):
        -           continue
        -       print(i)
        - o/p =>0 1 2 3 4 5 7 8 9
    - **pass**
        - Whenever block is defined it is always expecting some functionality but there might be situation when we are not in a situation to define or would want to define it in the future then in the body of block we can mention it as pass.
        - statement following after pass keyword in the asme block will also be executed  
        - It can be used in class, function, control statement 
        -     class passExample:
        -         pass 
    

## else conditional statement with loop (for, while)
**The else block just after for/while is executed only when the loop is NOT terminated by a break statement**.                                                  
https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/                                                               
- not applicable with continue , else will always execute when continue is present                      

## del :-
- syntax:- **del varName or del(varName)**
- we can use del keyword **to delete a variable**
- After del, automatically the corresponding object is elligble for garbage collection (GC).
- Garbage Collector is responsible to destroy objects, **del job is only to delete the vaiable (not to delete object)** and make it eligible for GC.
- eg
    - var = [10,20,3,0]
    - del(var[0])  or  del var[0]   => var => [20,30]
    - del(var)     or  del var      => var => error

| **del var or del(var)** | **var = None** |                                                       
| ----------------------- | -------------- |                                                                                  
| This means var itself is deleted. It is no longer refrensing to any object. Accesing this var will result in error. | But this means wouln't delete the var, infact it will make it reference to None and if someone is trying to access or print(var) this will not give error. |


