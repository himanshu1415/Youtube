def isdecimalIsIdentifierFunction():
    
    # isdecimal - only base 10 numbers are allowed
    text = "123" 
    #text = "a123"
    #text = "⅔"
    #text = "2/3"
    #text = "2²"
    #text = "ↁ"
    print(text.isdecimal())

    # isIdentifier
    text = "validString"
    # returns true if string is a valid identifier
    # string is considered valid if it contains alphanumeric 
    # or underscore. Can not start with number or contain any spaces
    #text = "CodersWorld_"
    #text = "n2d_Valid"
    #text = "Like Share Comment"
    print(text.isidentifier())

isdecimalIsIdentifierFunction(