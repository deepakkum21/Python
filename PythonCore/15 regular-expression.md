# Python Regular Expression
- If we want to represent a group of strings according to a particular  pattern then we use RE.
- a regular expression could tell a program to search for specific text from the string and then to print out the result accordingly. 
- Expression can include
    - Text matching
    - Repetition
    - Branching
    - Pattern-composition etc 
- **re module** is used

### Application of ----------
- Validations
- Pattern Matching
- Translators like interpreters, assemblers, compilers
- to develop digital circuits using FiniteAutomata using moore and melay


### to find the start index and end index with no of occurrences
                import re                                                                                   
                count = 0                                                                           
                pattern = re.compile('ab')                                                                           
                matcher = pattern.finditer('abbaababb')   # matcher = re.finditer('ab', 'abbaababb')                                                           
                for match in matcher;                                                                           
                    count+=1                                                                           
                    print('match is available at start index: ',match.start())                                                                           
                    print('match is available at end index: ',match.end()-1)                                                                           
                    print('match is available for: ',match.group())                                                                           
                print('The number of occurrences: ',count)     



| **Character classes** | **Description** |                                                                               
| --------------------- | --------------- |                                                                                               
| [abc] | either a or b or c |
| [^abc] | except abc |
| [a-z] | Any lowercase alphabet symbol |
| [^a-z] | except lowercase alphabet symbol |
| [A-Z] | Any uppercase alphabet symbol |
| [^A-Z] | except uppercase alphabet symbol |
| [a-zA-Z] | Any lowercase or uppercase alphabet symbol |
| [^a-zA-Z] | except lowercase or uppercase alphabet symbol |
| [0-9] | any digit |
| [^0-9] | except digit |
| [0-9A-Ba-b] | any digit or lowercase or uppercase |
| [^0-9A-Ba-b] | except digit or lowercase or uppercase |                                                                                          

| **Predefined Character classes** | **Description** |                                                                               
| --------------------- | --------------- | 
| \s | space (tab,space,newline etc.) equivalent to [ \t\n\r\f\v] |  
| \S | anything except a space equivalent to [^ \t\n\r\f\v] |
| \d | any digit equivalent to [0-9]. |
| \D | except digit equivalent to [^0-9].|
| \w | letters ( Match alphanumeric character, including "_") equivalent to [a-zA-Z0-9_] |
| \W | Matches any character which is not a word character equivalent to [^a-zA-Z0-9_] | 
| .  | matches every character |     

| **Quantifiers** | **Description** |                                                                               
| --------------- | --------------- | 
| a+ | matches 1 or more a (atleast 1 or more a) |
| a* | 0 or more a (any no of a including 0 no of a | 
| a? | atmost 1 no of a (either 0 no of a or atmost 1 no of a) |
| a{x} | exactly x no of a |
| a{m,n} | minimum m no of a and maxixmum n no of a | 
| ^a | check whether the string start with a or not | 
| a$ | check whether the string ends with a or not | 
