# Python Regular Expression
- If we want to represent a group of strings according to a particular  pattern then we use RE.
- a regular expression could tell a program to search for specific text from the string and then to print out the result accordingly. 
- Expression can include
    - Text matching
    - Repetition
    - Branching
    - Pattern-composition etc 
- **re module** is used

### Application of RE :-
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
| \w | letters ( Match alphanumeric character, including ' _ ') equivalent to [a-zA-Z0-9_ ] |
| \W | Matches any character which is not a word character equivalent to [^a-zA-Z0-9_ ] | 
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



| **Imp RE functions** | **Description** |         
| -------------------- | --------------- |                                                                                                    
| match() | to check the given pattern at the beginning of the string . if then returns  corresponding match object Else it returns None, if the string does not match the given pattern. | 
| fullmatch() | to check the given pattern matches with the whole target string if then returns  corresponding match object Else it returns None |                    | search() | scan through the given string/sequence looking for the first location where the regular expression produces a match. It returns a corresponding match object of the first occurrence if found, else returns None  | 
| findall() | it returns a list having all the items which are matched |   
| finditer() | it returns iterator of matched objects |
| sub() | It returns the string obtained by replacing or substituting the leftmost non-overlapping occurrences of pattern in string by the replacement repl. If the pattern is not found then the string is returned unchanged. | 
| subn() | same operation as sub(), but return a tuple (new_string, number_of_subs_made). |  
| split() | Split string by the occurrences of pattern. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list. |


more imp function:- (https://docs.python.org/3/library/re.html)

**eg of match()**
-               import re
                inputstring = input('Enter the pattern to check: ')
                matchstring = re.match(inputstring, 'abhfbcmbkakbca')
                if matchstring != None:
                    print('Found the match string at the beginning of the target string using match() at starting index: {} and end index: {}'.format(matchstring.start, matchstring.end()-1))
                else:
                    print('Didn't found the match string')

**eg of fullmatch()**
-               import re
                inputstring = input('Enter the pattern to check: ')
                matchstring = re.fullmatch(inputstring, 'abhfbcmbkakbca')
                if matchstring != None:
                    print('Found the full match string )
                else:
                    print('Didn't found the full match string')                

**eg of search()**
-               import re
                inputstring = input('Enter the pattern to check: ')
                matchstring = re.search(inputstring, 'abhfbcmbkakbca')
                if matchstring != None:
                    print('Found the full match string )
                else:
                    print('Didn't found the full match string')    


**eg of findall()**
-               import re
                matchlist = re.findall('[0-9], '86fgd0ghgf34534')
                print(matchlist)          

**eg of finditer()**
-               import re
                inputstring = input('Enter the pattern to check: ')
                matchiter = re.finiter(inputstring, 'abhfbcmbkakbca')
                for match in matchiter:
                    print(type(match))
                    print(maych)   

**eg of sub(pattern, repl, string, count=0, flags=0)**
- *repl can be a string or a function*
-               import re
                inputstring = input('Enter the pattern to replace: ')
                targetstring = input('Enter the Target String : ')
                replacedString = re.sub(inputstring, '#', targetstring)
                print(replacedString)
- repl as a function                                                                                                 
                def dashrepl(matchobj):
                    if matchobj.group(0) == '-': 
                        return ' '
                    else: 
                        return '-'
                re.sub('-{1,2}', dashrepl, 'pro----gram-files')     # 'pro--gram files'  

**eg of subn(pattern, repl, string, count=0, flags=0)**
-               import re
                inputstring = input('Enter the pattern to replace: ')
                targetstring = input('Enter the Target String : ')
                resultTuple = re.sub(inputstring, '#', targetstring)
                print(resultTuple)   
                print('The result string' + resultTuple[0]) 
                print('The no of replacements' + resultTuple[1]) 

**eg of split(pattern, string, maxsplit=0, flags=0)**
-               stringList = re.split('-', 'deepak-kumar')    

**eg of valid 10, 11, 12, 13 digit mb no**
-               print(re.fullmatch('(0|91|\+91)?[6-9]\d{9}',input('ENETER THE MB NO.')))

**To extract all mb no from a .txt file**
-               import re
                file1 = open('input.txt', 'r')
                file2 = open('output.txt', 'w')
                for line in file2:
                    lineresultlist = re.findall('[6-9]\d{9}, line)
                    for item in lineresultlist:
                        file2.write(item + '\n')
                print('Extracted all valid mb no from input file and witten to output file')
                file1.close()
                file2.close()

**eg of web scrapping to find title**
-               import re, urllib
                import urllib.request
                sites = ['https://goggle.com', 'https://facebook.com']
                for site in sites:
                    print('searching......', site)
                    u = urllib.request.urlopen(site)
                    textVersion = u.read()
                    title = re.findall("<titel>.*</title>", str(textVersion), re.IGNORECASE)
                    print(title)

**eg of web scrapping to find all valid mb no from redbus.in**
-               import re, urllib
                import urllib.request    
                u = urllib.request.urlopen(site)
                textVersion = u.read()                
                numberlist = re.findall('[0-9]{3,4}[- ][0-9]+', textVersion)
                for number in numbers:
                    print(number)


