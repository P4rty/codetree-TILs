n = 3
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]
arr_2d1 = [
    #[0 for _ in range(n)]
    #for _ in range(n)
]
arr_2d2 = [
    #[0 for _ in range(n)]
    #for _ in range(n)
]

for i in range(3):
    arrk = list(map(int,input().split()))
    arr_2d1.append(arrk)
input()

for i in range(3):
    arrk = list(map(int,input().split()))
    arr_2d2.append(arrk)

for i in range(3):
    for j in range(3):
        arr_2d[i][j]=arr_2d1[i][j]*arr_2d2[i][j]

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()