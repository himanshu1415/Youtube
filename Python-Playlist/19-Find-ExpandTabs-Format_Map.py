def stringMoreFunctions():
    # ExpandTabs
    text = "E\tX\tP\tA\tN\tD"
    print(text.expandtabs())
    print(text.expandtabs(2))
    
    # Find
    text = "Like Share & Subscribe CodersWorld"
    print(text.find('Coder'))
    print(text.find('Content'))
    print(text.find('Share',0))
    print(text.find('Like',10,20))
    print(text.find('CodersWorld',-12))

    # format_map
    point = {'lat':72,'lon':27}
    print('{lat} {lon}'.format_map(point))

    print(text)

stringMoreFunctions()