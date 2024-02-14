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
for i in range(1,N):
    if arr[i] != arr[i-1]:
        if cnt > maxe :
            maxe = cnt
        cnt=1
    else:
        cnt += 1
        if i == N-1 and cnt > maxe:
            maxe = cnt -1
print(maxe)