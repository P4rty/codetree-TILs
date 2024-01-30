n,m= map(int,input().split())

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]
value = 0
num = 0
while value < n*m :
    for i in range(num+1):
        for j in range(num+1):
            if i>=n or j >=m:
                continue
            if i+j ==num:
                value+=1
                arr_2d[i][j]=value
    num +=1


for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()