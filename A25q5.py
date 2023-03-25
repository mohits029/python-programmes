a= [[1,3,4],[2,3,4],[5,4,3]]
b= [[4,3,2],[1,2,3],[8,9,1]]

for i in range(0,3):
    for j in range(0,3):
        print(a[i][j]+b[i][j], end="\t")

    print()