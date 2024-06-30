def ComparisonOperator():
    #1. == (Equal Operator)   
    x = 22
    y = 23
    #print(x == y)

    #2. != (Not Equal Operator)  
    #print(x != y)

    #3. > (Greater Than Operator)  
    #print(x > y)

    #4. < (Less Than Operator)  
    #print(x < y)

    #5. >= (Greater Than or Equal To Operator)  
    #print(x >= y)

    #6. <= (Less Than or Equal To Operator)  
    print(x <= y)

ComparisonOperator()

def IdentityOperator():
    # Python Identity Operators
    # Identity operators are used to compare the objects, not if they are equal, 
    # but if they are actually the same object, with the same memory location:

    originalFruitList1 = ["apple", "banana"]
    originalFruitList2 = ["apple", "banana"]
    copyFruitList = originalFruitList1

    #print(originalFruitList1 is copyFruitList)
    # returns True because z is the same object as x

    #print(originalFruitList1 is originalFruitList2)
    # returns False because x is not the same object as y, 
    # even if they have the same content

    print(originalFruitList1 == originalFruitList2)

IdentityOperator()