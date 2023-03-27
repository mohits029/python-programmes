

blackhat= eval(input("Enter name of black-hat seprated by comma: "))
redshose= eval(input("Enter name of red-shoose candidate seprated by comma"))

blackhat=set(blackhat)
redshose=set(redshose)


print(blackhat.intersection(redshose))