def stringMoreFunctions():
    #1. capitalize
    text = "python Can be Fun"
    text = text.capitalize()
    
    text = "1000 Subscribers is my Target."
    text = text.capitalize()
    
    #2. casefold and Lower
    text = "ß"
    text = text.lower() 
    text = text.casefold()

    #3. Center
    text = "CodersWorld" 
    text = text.center(21)
    text = text.center(121,'-')

    #4. Count
    text = "Agar ab tak video dekh rahe to video like kardo and comment kardo"
    print(text.count('video'))
    print(text.count('video',16))
    print(text)

stringMoreFunctions()