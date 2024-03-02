def variableFunctions():
    # Many Values to Multiple Variables
    number1,number2,number3 = 1,2,3
    """print(number1)
    print(number2)
    print(number3)"""
    
    # One Value to Multiple Variables
    number1 = number2 = number3 = "Sample"
    print(number1)
    print(number2)
    print(number3)

def printFunctions():
    x = "Like"
    y = "Share"
    z = "Subscribe CodersWorld"
    #print(x, y, z)
    #print(x + y + z)

    a=2
    b="test"
    #print(a+b)  #Q1 will this work
    print(a,b)  #Q2 will this work
variableFunctions()
printFunctions()