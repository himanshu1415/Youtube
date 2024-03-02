def dataTypesInPython():
    #Text Type:	str
    #x = "Hello World"
    #Numeric Types:	int, float, complex
    #x = 10
    #x = 10.5
    #x = 10j
    #x = complex(1j)
    #Sequence Types: list, tuple, ranged
    #x = ["1", "2", "3"]
    #x = ("1", "2", "3")
    #x = range(6)
    #Mapping Type:	dict
    #x = {"name" : "Himanshu", "age" : 24}
    #Set Types:	set, frozenset
    #x = {"c++", "python", "java","c++"}
    #x = frozenset({"c++", "python", "java"})
    #Boolean Type:	bool
    #x = True
    #Binary Types:	bytes, bytearray, memoryview
    x = bytes([65,66,67])  
    x = bytearray([65,66,67])
    byte_arr = bytes([65,66,67])
    x = memoryview(byte_arr)
    #None Type:	NoneType
    x = None
    print("Value of x ",x,", Type of Variable ",type(x))

dataTypesInPython()