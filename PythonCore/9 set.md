# Set

1. To represent group of individual object where order is not important.
2. Insertion order is **not** preserved.
3. Duplicate object are not allowed.
4. if duplicate object are present would eliminate itself by storing unique one.
5. it doesnot support indexing , slicing
    - eg s = {10,20,30}   => s[0]   => invalid (since they are unordered)
6. It is **mutable** 
7. It is dynamic :-
    - .add() -> to increase the size
    - .remove() -> to decrease the size 
8. use loop to get the data 
    - for x in s : print(x)
9. s = {} is dict not set
10. To create empty set 
    **emptySet = set()**    

### How to create a set?
1. **emptySet = set()**  
2. A set is created by placing all the items (elements) inside curly braces {}, separated by comma
    - setVar = {1,2,3,4,5}
3. It can have any number of items and they may be of **different types (integer, float, tuple, string etc.)**. 
    - my_set = {1.0, "Hello", (1, 2, 3)}
4. But a **set cannot have a mutable element, like list, set or dictionary, as its element**.
    - my_set = {1.0, "Hello", {1, 2, 3}}  => invalid  (set not hashable)
    - my_set = {1.0, "Hello", [1, 2, 3]}  => invalid  (list not hashable) 
    - my_set = {{1:1}, "Hello", (1, 3)}   => invalid  (dict not hashable)

### How to Access set elements:
- **since they are unordered, indexing have no meaning.**
- using index => not applicable
- using slice operator => not applicable                                                                                                  


### How to remove elements from a set?
1.  item can be removed from set using methods, 
    - **discard() => if the item does not exist in the set, it remains unchanged**
    - **remove() => if the item does not exist in the set, raise an error in such condition**. 
    - **pop() => Set being unordered, there is no way of determining which item will be popped. It is completely arbitrary.**
    - **clear() => to remove all elements of the set**

### Set Operations :-
- Union ( union() or | )
- Intersection ( intersection() or & )
- Difference ( difference() or - )
- Symmetric Difference ( symmetric_difference() or ^ )

1. **Union operation ( union() or | )**
    - Union of A and B is a set of all elements from both sets.
    -       A = {1, 2, 3, 4, 5}
    -       B = {4, 5, 6, 7, 8}
    -       print(A | B)   or  A.union(B)
    -       Output: {1, 2, 3, 4, 5, 6, 7, 8}
2. **Intersection operation ( intersection() or &)**
    - Intersection of A and B is a set of elements that are common in both sets.
    -       A = {1, 2, 3, 4, 5}
    -       B = {4, 5, 6, 7, 8}
    -       print(A & B)   or  A.intersection(B)
    -       Output: {4, 5}     
3. **Difference operation ( difference() or - )**  
    - Difference of A and B (A - B) is a set of **elements that are only in A but not in B**. 
    - Similarly, **B - A is a set of element in B but not in A**.
    -       A = {1, 2, 3, 4, 5}
    -       B = {4, 5, 6, 7, 8}
    -       print(A - B)   or  A.difference(B)
    -       Output: {1, 2, 3} 
4. **Symmetric Difference operation ( symmetric_difference() or ^ )**
    - Symmetric Difference of A and B is a set of elements in both A and B **except those that are common in both**.
    -       A = {1, 2, 3, 4, 5}
    -       B = {4, 5, 6, 7, 8}
    -       print(A ^ B)   or  A.symmetric_difference(B)
    -       Output: {1, 2, 3, 6, 7, 8}

### Set methods

| **Method** | 	**Description** |                                                                            
| ---------- | ---------------- |                                                                                                         
| add() | 	Adds an element to the set | 
| clear() | 	Removes all elements from the set | 
| copy() | 	Returns a copy of the set | 
| difference() | 	Returns the difference of two or more sets as a new set | 
| difference_update() | 	Removes all elements of another set from this set | 
| discard() | 	Removes an element from the set if it is a member. (Do nothing if the element is not in set) | 
| intersection() | 	Returns the intersection of two sets as a new set | 
| intersection_update() | 	Updates the set with the intersection of itself and another | 
| isdisjoint() | 	Returns True if two sets have a null intersection | 
| issubset() | 	Returns True if another set contains this set | 
| issuperset() | 	Returns True if this set contains another set | 
| pop() | 	Removes and returns an arbitary set element. Raise KeyError if the set is empty | 
| remove() | 	Removes an element from the set. If the element is not a member, raise a KeyError | 
| symmetric_difference() | 	Returns the symmetric difference of two sets as a new set | 
| symmetric_difference_update() | 	Updates a set with the symmetric difference of itself and another | 
| union() | 	Returns the union of sets in a new set | 
| update() | 	Updates the set with the union of itself and others |   

### Built-in methods which take set as arg

| **Function** |	**Description** |                                                                
| ------------ | ------------------ |                                                                               
| all() |  	Return True if all elements of the set are true (or if the set is empty). |  
| any() |  	Return True if any element of the set is true. If the set is empty, return False. |  
| enumerate() |  	Return an enumerate object. It contains the index and value of all the items of set as a pair. |  
| len() |  	Return the length (the number of items) in the set. |  
| max() |  	Return the largest item in the set. |  
| min() |  	Return the smallest item in the set. |  
| sorted() |  	Return a new sorted list from elements in the set(does not sort the set itself). |  
| sum() |  	Retrun the sum of all elements in the set. |  