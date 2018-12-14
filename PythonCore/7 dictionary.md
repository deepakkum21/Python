## dict :-
1. To represent group of individual object as key-value pairs.
2. Key :
    - duplicates are not allowed.
    - hetrogenous object is allowed
    - key **can be tuple but not list**
3. Value :
    - duplicates are allowed.
    - hetrogenous object is allowed
4. To add key-value in existing dict
    eg: p = {101:'deepak'}   =>  p[key] = value  => p[102] = 'abc'   => p  => {101:'deepak', 102:'abc'}
5. it is **mutable**
6. Insertion order not preserved.
7. if *trying to add duplicate key but value is different , wouldn't give erroe but it will override the previous value with the new value* for that key which was duplicate.

### How to create dict
1. empty dict , dictvar = {} or dictVar = dict()
2. dictVar = dict() 
    -          dictVar[key] = value
3. dictVar = dict([(100,'deepak'), (101,'ashif'), (102,'rakesh')])   => valid 
    - instead of list, we can take set or tuple
    - instead of tuple, we can take set or tuple
    - but we should take only two elements inside 


### to access dict data
1. **by using key**
    - if key in dicvar: print(dicVar[key])

## To delete elements from dict
1. del dictVar[key]   or del(dictVar[key])
2. deleting key removes corresponding value from dictionary


### dict methods

| **Method**	| **Description** |                                                                                                                   
| ------------- | --------------- |                                                                                                    
| clear() |	Remove all items form the dictionary. |
| copy() |	Return a shallow copy of the dictionary. |
| fromkeys(seq[, v]) |	Return a new dictionary with keys from seq and value equal to v (defaults to None). |
| get(key[,d]) |	Return the value of key. If key doesnot exit, return d (defaults to None). |
| items() |	Return a new view of the dictionary's items (key, value). |
| keys() |	Return a new view of the dictionary's keys. |
| pop(key[,d]) |	Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError. |
| popitem() |	Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty. |
| setdefault(key[,d]) |	If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None). |
| update([other]) |	Update the dictionary with the key/value pairs from other, overwriting existing keys. accepts only one arg. |
| values() |	Return a new view of the dictionary's values |                         

### Built in function that take dict as arg

| **Function**	| **Description** |                    
| ------------- | --------------- |                                          
| all() | 	Return True if all keys of the dictionary are true (or if the dictionary is empty). | 
| any() | 	Return True if any key of the dictionary is true. If the dictionary is empty, return False. | 
| len() | 	Return the length (the number of items) in the dictionary. | 
| cmp() | 	Compares items of two dictionaries. | 
| sorted() | 	Return a new sorted list of keys in the dictionary. | 

### dict comprehension: 
1. Dictionary comprehension is an elegant and concise way to create new dictionary from an iterable in Python.
2. consists of an expression pair (key: value) followed by for statement inside curly braces {}.
    - **{x: x*x for x in range(6)}**   => return dict
3. A dictionary comprehension can optionally contain more for or if statements.
    - **odd_squares = {x: x*x for x in range(11) if x%2 == 1}**


### Dictionary Membership
1. **in**
    - can test if a key is in a dictionary or not using the keyword in , but not for values.