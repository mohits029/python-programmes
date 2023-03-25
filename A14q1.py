x= int(input("Enter a three digit number: "))

match x:
    case x if x>99 and x<999:
        print("3 digit number")
    case x:
        print("Not a 3 digit number")