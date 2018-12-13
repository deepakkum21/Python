# List and Tuple

## List
1. To represent group of individual object as a single entity.
2. Insertion order is preserved.
3. Duplicate object are allowed.
4. Hetrogeneous objects are allowed.
5. It is **mutable** 
6. It is dynamic :-
    - .append() -> to increase the size
    - .remove() -> to decrease the size
7. eg listVarible = ['deepak', 10, true, 45.2]
8. **to take list from keyboard**
    - use **eval()** 
    -    listInput = eval(input('Enter List of Values: '))
    - Enter List of Values: [1,5,32,6,7,]
    - type(listInput)  => <class 'list'>
9. **to convert to list from any sequence** (string, range, tuple, set)
    - use **list()**
    - list() takes only one argument.
    - listVar = list(range(2,8,2))  => listVar = [2,4,6,8]
10. by **using split()** 
    - default separator for split() is space
    - stringVar = 'Hi how are you'
    - listVar = stringVar.split()   => listVar = ['Hi', 'how', 'are', 'you']
    - split() can only be called on the string type

### How to Access list elements:
- using index
    - raises indexError when the index which you want to access is not present
- using slice operator
    - doesnot raise any error if the desired index is not present

### Accessing list with loop:
1. **for**
    - for x in listVar: do something
2. **while**
    - while x < len(listVar) : do something

### Python list methods:

| **List Methods** | **Description** | **Example listvar.methodName()** |                                                                                           
| ---------------- | --------------- | -------------------------------- |                                                                              
| append() | Add an element to the end of the list |    listvar.append(value_to_be_inserted_to_list)        |          
| extend() | Add all elements of a sequence to the another list. Takes only one arg |   listvar.extend(sequenceVar)  -> sequenceVar: can be string, list, tuple, set       |
| insert() | Insert an item at the defined index |  listvar.insert(index, value_to_be_inserted_to_list)          |          
| remove() | Removes an item from the list. If the specified value  which is needed to be removed, will get error . If multiple occurrences of that specified value is there then only first occurred value will be removed|  listvar.remove(value_to_be_removed_to_list)  | 
| pop() | Removes and returns an element at the given index. if index not specified it will take last index as argument. list length should not be zero otherwise error | listvar.pop() -> removes and return last value of list ,  listVar.pop(index) -> removes and return value at specified index  |    
| clear() | Removes all items from the list. Makes list Empty |    listVar.clear()        |          
| index() | Returns the index of the first matched item |            |          
| count() | Returns the count of number of items passed as an argument |            |          
| sort() | Sort items in a list in ascending order . if desecending order in needed sort(reverse=True) |  listVar.sort() -> asc , listVar.sort(reverse=True) -> desc |
| reverse() | Reverse the order of items in the list |   listVar.reverse()         |          
| copy() | Returns a shallow copy of the list .This will create a different object with same elements |  listVar.copy()          |  


| **reverse()** | **reversed()** |                                                                                                                  
| ------------- | -------------- |                                                                                           
| it is list specific method | it is python in-built method |                
| it returns a list by reversing the order of elements present in the list | it returns a object which has reversed elements but to get those elements using loop |  

| **sort()** | **sorted()** |                                                                                                                  
| ---------- | ------------ |        
| it is list specific method | it is python in-built method |            
| it returns a list by sorting it in ascending order | it also returns a list by sorting it in ascending order |  

### Methods which take list as arg:-

| **Method** | **Description** | **example methodName(listVar)** |   
| ---------- | --------------- | ------------------------------- |              
| any() |	Checks if any Element of an Iterable is True |                    |                     
| all() |	returns true when all elements in iterable is true |                    |                     
| ascii() |	Returns String Containing Printable Representation |                    |                     
| bool() |	Converts a Value to Boolean |                    |                     
| enumerate() |	Returns an Enumerate Object |                    |                     
| filter() |	constructs iterator from elements which are true |                    |                     
| iter() |	returns iterator for an object |                    |                     
| list() | Function	creates list in Python |                    |                     
| len() |	Returns Length of an Object |                    |                     
| max() |	returns largest element |                    |                     
| min( |)	returns smallest element |                    |                     
| map() |	Applies Function and Returns a List |                    |                     
| reversed() |	returns reversed iterator of a sequence |                    |                     
| slice() |	creates a slice object specified by range() |                    |                     
| sorted() |	returns sorted list from a given iterable |                    |                     
| sum() |	Add items of an Iterable |                    |                     
| zip() |	Returns an Iterator of Tuples |                    |                     


### Aliasing :
- providing duplicate name is aliasing
- eg: listVar = [10,20]    ,   listVar2=listVar
- both listVar and listVar2 will be pointing to the same object
- has disadvantage 
    - changes performed using one will be reflected on the other with those changes

### Cloning concept:
1. this can be achieved using 
    - **copy()**
        - Returns a shallow copy of the list .
        - This will create a different object with same elements
    - **slice[begin:end:step]** (default value: begin=1, end=len, step=1)
        - This will return a new list with elements from begin to end-1

### Mathematical operators for list object ( + , *)
1. **(+) operator** 
    - this works same as extend() , i.e. it adds the second list to end of 1st list object and **compulsory new object will be created**.
    - for using + **both argument must be list**
    - eg: list1 = [1,2,3,4,5,6,7] ,     list2 = [8,9],    => list3 = list1 + list2 (valid)
    - eg: list1 = [1,2,3] ,     => list3 = list1 + 3 (invalid)
2. **(*) operator**
    - it make list to repeat 
    - eg: list1 = [1,2,3,4] * 3    => [1,2,3,4,1,2,3,4,1,2,3,4]

3. **(<,>) operator** 
    - these operator (<,>) will only comapre the first elements of the both the list
        - eg list1 > list2   => [10,20,30] > [10,20,40]
        - if first element of both list is same then it checks the other element for both list till it gets the result True or False

4. **(in, not in) membership operator**
    - whether the element is present or not
    - 3 in [1,2,3]

### list packing and Unpacking
1. **list packing**
    -     a = 1  
    -     b = 2 
    -     c = 3 
    -     d = 4
    -     listVar = [a, b, c, d]
    -     print(listVar)  => [1,2,3,4]   
2. **list unpacking**
    -     listVar = [2,3,7,8]
    -     a, b, c, d = listvar
    -     print('a = {} ,b = {} , c = {} ,d = {}'.format(a,b,c,d))     =>  a = 2, b = 3, c = 7, d = 8


### Nested List
- listVar = [1,2,3,[4,5,6],7]

## List Comprehension 
1. listVar = [x for x in range(1,11)]   => lsitVar = [1,2,3,4,5,6,7,8,9,10]
2. can also perform extra activity
    - listVar = [x for x in range(1,11) if x%2]             
3. syntax: **[expression for x in sequence condition]**
    - to get list of values present in both list l1 and l2
        - [x for x in l1 if x in l2]
    - to get list of values present in list l1 but not in list l2
        - [x for x in l1 if x not in l2]



## Tuple (immutable list)
1. To represent group of individual object as a single entity.
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

### How to create tuple:-
1. empty tuple:- tupVar = ()
2. single value tuple:- tupVar = (5,)
3. multi value tuple:- tupVar = (4,8,6)
4. from sequence:- tupVar = tuple(sequence)  -> sequence can be string, list, range, set

### How to Access tuple elements:
- using index
    - raises indexError when the index which you want to access is not present
- using slice operator
    - doesnot raise any error if the desired index is not present

### Accessing tuple with loop:
1. **for**
    - for x in tupleVar: do something
2. **while**
    - while x < len(tupleVar) : do something

### Python Tuple Methods
Methods that add items or remove items are not available with tuple. Only the following two methods are available.

| **Tuple Method** | **Method	Description** |
| ---------------- | ------------------------ |                                                                                                     
| count(x) |	Return the number of items that is equal to x |
| index(x) |	Return index of first item that is equal to x |       

### Python built-in function which take tuple as arg

| **Function** |	**Description** |                     
| ------------ | ------------------ |                                                           
| all() |	Return True if all elements of the tuple are true (or if the tuple is empty). |
| any() |	Return True if any element of the tuple is true. If the tuple is empty, return False. |
| enumerate() |	Return an enumerate object. It contains the index and value of all the items of tuple as pairs. |
| len() |	Return the length (the number of items) in the tuple. |
| max() |	Return the largest item in the tuple. |
| min() |	Return the smallest item in the tuple |
| sorted() | Take elements in the tuple and return a **new sorted list** (does not sort the tuple itself). If want reverse order, then => tupleVar.sorted(reverse=True) |
| sum() |	Retrun the sum of all elements in the tuple. |
| tuple() |	Convert an iterable (list, string, set, dictionary) to a tuple. |


### Mathematical operators for tuple object ( + , *)
1. **(+) operator** 
    - this works same as extend() , i.e. it adds the second tuple to end of 1st tuple object and **compulsory new object will be created**.
    - for using + **both argument must be tuple**
    - eg: tuple1 = (1,2,3,4,5,6,7) ,     tuple2 = (8,9),    => tuple3 = tuple1 + tuple2 (valid)
    - eg: tuple1 = (1,2,3) ,     => tuple3 = tuple1 + 3 (invalid)
2. **(*) operator**
    - it make tuple to repeat 
    - eg: tuple1 = (1,2,3,4) * 3    => (1,2,3,4,1,2,3,4,1,2,3,4)

3. **(<,>) operator** 
    - these operator (<,>) will only comapre the first elements of the both the tuple
        - eg tuple1 > tuple2   => (10,20,30) > (10,20,40)
        - if first element of both tuple is same then it checks the other element for both tuple till it gets the result True or False

4. **(in, not in) membership operator**
    - whether the element is present or not
    - 3 in (1,2,3) 

### Tuple packing and Unpacking
1. **tuple packing**
    -     a = 1  
    -     b = 2 
    -     c = 3 
    -     d = 4
    -     tupleVar = a, b, c, d
    -     print(tupleVar)  => (1,2,3,4)   
2. **tuple unpacking**
    -     tupleVar = (2,3,7,8)
    -     a, b, c, d = tuplevar
    -     print('a = {} ,b = {} , c = {} ,d = {}'.format(a,b,c,d))     =>  a = 2, b = 3, c = 7, d = 8
3. can raise value error like too many and too less value to unpack if no of elements in tuple is not equal to the no of variable in which it is assigned 


### Tuple comphression
1. tuple comprehension is not applicable on Tuple
2. var = (x for x in range(1,11))   this would not give tuple **but will give generator object** throuh which we can derive value by iterating it.
    -  type(var)   =>   <class 'generator'>  but can manually convert to tuple by type casting it (tuple(var))


