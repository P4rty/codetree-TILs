a,b = map(int,input().split())

arr = [[0]*a for _ in range(a)]

for i in range(b):
    r,c = map(int,input().split())
    arr[r-1][c-1] = 1

for i in range(a):
    for j in range(a):
        print(arr[i][j],end=" ")
    print()