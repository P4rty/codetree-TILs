N = int (input())
arr = []
for _ in range(N):
    a = int(input())
    if a > 0 :
        arr.append(1)
    else:
        arr.append(0)

cnt = 1
maxe =1
for i in range(N):
    if arr[i] != arr[i-1]:
        if cnt > maxe or i == N:
            maxe = cnt
        cnt=1
    else:
        cnt += 1
        if arr[i]==N-1:
            maxe = cnt -1
print(maxe)