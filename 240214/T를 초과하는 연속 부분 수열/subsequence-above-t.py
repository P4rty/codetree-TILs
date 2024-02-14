N, t = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
maxe = 0
for i in range(N):
    if arr[i] <= t:
        if cnt > maxe :
            maxe = cnt
        cnt = 0
    else:
        cnt += 1
        if i == N-1 and cnt > maxe:
            maxe = cnt
print(maxe)