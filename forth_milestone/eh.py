while(1):
    try:
       x=int(input("enter x number"))
       y=int(input("enter y number"))
       a=x/y
       print(a)
    except ZeroDivisionError as e:
        print(e)
        print("Dont give the value of y zero")
