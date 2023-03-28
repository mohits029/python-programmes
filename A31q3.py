d1= {}

flag= True


while flag:
    player_name= input("Enter player Name: ")
    val= eval(input("Enter matches, total-runs, half-centuries, centuries recpectivly seprated by comma: "))
    d1.update({player_name:val})

    x= input("Enter Y to continue else Press N: ")
    if x== 'N'or x== 'n':
        flag=False

print(d1)