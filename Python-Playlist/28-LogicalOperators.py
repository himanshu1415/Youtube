def LogicalOperator():
    # Logical Operator
    conditionTrue = True
    conditionFalse = False

    #Truth Table
    '''
           Operand 1 | Operand 2 | Type of Operation
                                   AND     OR
            False     False       False   False
            False     True        False   True
            True      False       False   True
            True      True        True    True

        Operator 1 | Type of Operation
                       Not
            False     True
            True      False 
    '''
    # Logical And Operator
    if(conditionTrue and conditionFalse):
        print("And Logical Operator")
    # Logical Or Operator    
    if(conditionFalse or conditionTrue):
        print("Or Logical Operator")
    # Logical Not Operator    
    if(not(conditionTrue)):
        print("Not Logical Operator")    
    
LogicalOperator()