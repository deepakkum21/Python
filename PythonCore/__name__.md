# __name__
1. `__name__` is a special variable that is being set by python .
2. If the source file is executed as the main program,(i.e. directly) the interpreter sets the __name__ variable to have a value “__main__”.
    -           # File1.py   
                print("File1 __name__ = {}".format( __name__ ))
                
                if __name__ == "__main__": 
                    print("File1 is being run directly")
                else: 
                    print("File1 is being imported")

                Output :
                File1 __name__ = __main__
                File1 is being run directly


    
3. If this **file is being imported from another module, `__name__` will be set to the module’s name**.
    -           # File2.py 
                import File1 

                print "File2 __name__ = %s" %__name__ 

                if __name__ == "__main__": 
                    print "File2 is being run directly"
                else: 
                    print "File2 is being imported"

                Output :
                File1 __name__ = File1
                File1 is being imported
                File2 __name__ = __main__
                File2 is being run directly
 