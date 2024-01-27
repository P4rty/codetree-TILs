n = int(input())
arr = list(map(int, input().split()))
while True:
    if len(arr) !=1:
        a = max(arr)
        b = arr.index(a)
    print(b + 1, end=" ")
    arr = arr[:b ]
    if b == 0:
        break