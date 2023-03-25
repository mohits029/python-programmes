x= eval(input("Enter a number: "))

match x:
    case x if type(x)== int:
        print("Monday")

    case x if type(x)==complex:
        print("Tuesday")

    case x if type(x)==float:
        print("Wednesday")

    case x if type(x)==bool:
        print("Thursday")

    case x:
        print("hello world")