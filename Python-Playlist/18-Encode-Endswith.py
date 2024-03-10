def stringMoreFunctions():
    #5. Encode
    text = "this is ß normal string"
    text = text.encode()           # UTF-8
    text = text.encode('utf-8',"backslashreplace")
    text = text.encode('ascii',"ignore")
    text = text.encode('ascii',"namereplace")
    text = text.encode('ascii',"replace")
    text = text.encode('ascii',"xmlcharrefreplace")
    text = text.encode('ascii','strict')

    # 6. EndsWith
    text = "ends with colon :"
    print(text.endswith(':'))
    print(text.endswith(':',0,2))
    print(text.endswith(':',-3))

    text = "All is Well It Ends Well"
    print(text.endswith('Well'))

    print(text)

stringMoreFunctions()