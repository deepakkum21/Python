# Garbage Collection
## What is Garbage Collection?
1. Garbage collection is the **process of cleaning shared computer memory which is currently being put to use by a running program when that program no longer needs that memory**. 
2. With Garbage collection, that chunk of memory is cleaned so that other programs (or same program) can use it again.

## Python Garbage Collection
1. The process of memory management in Python is straightforward. Python **handles its objects by keeping a count to the references each object have in the program**, which means, **each object stores how many times it is referenced in the program**. 
2. This count is updated with the program runtime and **when it reaches zero**, this **means it is not reachable from the program anymore**. Hence, the memory for this object can be reclaimed and be freed by the interpreter.
3. eg
    -                   class User(object):
                        # this method is called when there is no ref to this class
                            def __del__(self):
                                print("No reference left for {}".format(self))

                        user1 = User()
                        user2 = user1
                        user3 = user1

                        user1 = None
                        user2 = None
                        user3 = None
                        # output
                        No reference left for <__main__.User object at 0x212bee9d9>
                        
4. 