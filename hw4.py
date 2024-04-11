def hello_print(a):
    msg1="Hello"+a
    msg2="Welcome to Seoul"
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    print("-"*nstr)
    print(msg1)
    print(msg2)
    print("-"*nstr)

hello_print(input("Input his/her name"))
