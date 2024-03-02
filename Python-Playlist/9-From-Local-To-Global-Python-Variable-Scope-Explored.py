globalVariableExample = "global variable"
#print("this is "+globalVariableExample)
#print("this is "+globalVariableInFunction)
def scopeOfVariables():
    globalVariableExample = "local variable"
    #print("this is "+globalVariableExample)
    global globalVariableInFunction 
    globalVariableInFunction = "global variable Created inside function"

scopeOfVariables()