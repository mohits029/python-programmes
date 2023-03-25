x= int(input("Enter a number: "))
match x:
    case x if x==0:
        print("zero")
    case x if x>0:
        print("positive")
    case x if x<0:
        print("Negative")