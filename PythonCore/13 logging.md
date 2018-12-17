# Logging

## logging Levels:-
1. CRITICAL  - 50 (default)
2. ERROR     - 40 (default)
3. WARNING   - 30 (default)
4. INFO      - 20
5. DEBUG     - 10
6. NOTSET    - 10

## How to implement
1. name of the file in which we want to store logging info
2. level messages- which logging level meassages you want to store messages
3. using **basicConfig() of logging** module
    - **logging.basicConfig(filename='log.txt', level=logging.WARNING)
4. function for calling
    - logging.debug(message)
    - logging.info(message)
    - logging.exception(meassage)
    - logging.warning(message)
    - logging.error(message)
    - logging.critical(message)

## Asert statement:-
- assert is used for debugging purposes.
- Assertions are the condition or boolean expression which are always supposed to be true in the code.
- assert statement takes an expression and optional message.
- assert statement is used to check types, values of argument and the output of the function.
- assert statement is used as debugging tool as it halts the program at the point where an error occurs.
- eg, **assert (Temperature >= 0),"Colder than absolute zero!"**
- types of assert statement:-
    1. Simple version
    2. Very simple Version (agumented version)
