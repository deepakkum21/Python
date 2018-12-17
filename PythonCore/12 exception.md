# Exception


## User Defined Exception:-
1. **raise** keyword is used to raise a user defined exception.
            class TooOldException(Exception)
                def __ init__(self, arg):    # constructor
                    self.msg=arg
            class TooYoungException(Exception)
                def __ init__(self, arg):
                    self.msg=arg
            age = int(input('Enter the age: ))
            if age > 60:
                raise TooOldException('You have already crossed the age of marraige')
            elif age < 18:
                raise TooYoungException('You are too young to be married')
            else:
                print('Your age correct for getting married')

![user-defined-exzception]()