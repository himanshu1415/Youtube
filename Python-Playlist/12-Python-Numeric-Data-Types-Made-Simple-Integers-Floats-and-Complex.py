def numericDataTypes():
    # 1. Int, or integer, is a whole number, positive or negative, without decimals, 
    # of unlimited length.
    x = 2
    y = 223344556788
    z = -1234567
    """print(type(x))
    print(type(y))
    print(type(z)) 
    """
    # 2. Float, or "floating point number" is a number, positive or negative, containing
    # one or more decimals.
    x = 2.10
    y = 2.0
    z = -12.59
    
    """print(type(x))
    print(type(y))
    print(type(z))"""
    # Float can also be scientific numbers with an "e" to indicate the power of 10.
    x = 35e3
    y = 12E4
    z = -87.7e100
    """print(type(x))     
    print(type(y))
    print(type(z))
    """
    # 3. Complex numbers are written with a "j" as the imaginary part:
    x = 2+1j
    y = 2j
    z = -6j
    print(type(x))
    print(type(y))
    print(type(z))

numericDataTypes()