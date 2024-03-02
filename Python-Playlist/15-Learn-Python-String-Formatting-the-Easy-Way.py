def stringDataTypes():
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