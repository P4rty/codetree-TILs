n,m= map(int,input().split())

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 0
for j in range(m):
    if j % 2 ==0:
        for i in range(n):
            arr_2d[i][j]=num
            num += 1
    else:
        for i in range(n-1,-1,-1):
            arr_2d[i][j]=num
            num += 1
    


for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()