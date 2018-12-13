# List
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

## How to Access list elements:
- using index
    - raises indexError when the index which you want to access is not present
- using slice operator
    - doesnot raise any error if the desired index is not present

## Accessing list with loop:
1. **for**
    - for x in listVar: do something
2. **while**
    - while x < len(listVar) : do something

## Python list methods:

| **List Methods** | **Description** | **Example listvar.methodName()** |                                                                                           
| ---------------- | --------------- | -------------------------------- |                                                                              
| append() | Add an element to the end of the list |            |          
| extend() | Add all elements of a list to the another list |            |          
| insert() | Insert an item at the defined index |            |          
| remove() | Removes an item from the list |            |          
| pop() | Removes and returns an element at the given index |            |          
| clear() | Removes all items from the list |            |          
| index() | Returns the index of the first matched item |            |          
| count() | Returns the count of number of items passed as an argument |            |          
| sort() | Sort items in a list in ascending order |            |          
| reverse() | Reverse the order of items in the list |            |          
| copy() | Returns a shallow copy of the list |            |        


## Methods which take list as arg:-

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
