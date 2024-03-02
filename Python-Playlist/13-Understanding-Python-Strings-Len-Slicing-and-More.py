def stringDataTypes():
    x = "hello world"
    x = """  Multiline
             String   
        """
    #print(x)
    y = '''  Second
             Type of Multiline
             String
        '''
    #print(y)
    z = "Sample"
    # length of string
    #print(len(z)) # each character taken one length
    #print("Sam" in z)
    #print("Sam" not in z)
    #      Index  0123456789  
    helloWorld = "Hello, World!"                          
    # slicing of string
    #print(helloWorld[2:5])
    #print(helloWorld[:5])
    #print(helloWorld[2:])
    #print(helloWorld[-5:-2])

    # To Lower  /  To Upper
    #print(helloWorld.lower());
    #print(helloWorld.upper());

    whiteSpacesStr = " string with start and end whitespaces "
    # Remove whitespace
    #print(whiteSpacesStr.strip())

    #Replace String
    #print(whiteSpacesStr.replace("s","i"))
    #print(whiteSpacesStr.replace("start","end"))

    # Split String
    #print(whiteSpacesStr.split("end"))

    # Format String
    age = 25
    #intro = "My name is Himanshu, I am " + age

    age = 25
    intro = "My name is Himanshu, and I am {}"
    #print(intro.format(age))

    channelName = "CodersWorld"
    subscribers = 400
    myorder = "My Channel is {} and has {}."
    #print(myorder.format(channelName, subscribers))

    price = 500
    item = 10
    quantity = 1
    myorder = "I want to buy {2} shirt for {0} of item {1}."
    print(myorder.format(price, item, quantity))

stringDataTypes()