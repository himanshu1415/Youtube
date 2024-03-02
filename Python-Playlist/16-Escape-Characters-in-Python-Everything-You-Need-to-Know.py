def EscapeCharacterInString():
    # Escape Character \

    # Why Escape Character is Used 
    # An escape character is a backslash \ followed by the character you want to insert
    #text = "I am Learning "Python""
    text = "I am Learning \\Python\""
    #print(text)
    # \'
    # \\
    # \n
    text = "I am Learning \r Python is bigger"
    #print(text)
    # \r
    # \t
    text = "I am Learning\tPython"  
    #print(text)
    # \b
    text = "I am Learning \bPython"
    #print(text)
    # \ooo
    text = "\110"
    #print(text)
    # \xhh
    text = "\x48"
    print(text)
    #\f7

EscapeCharacterInString()    