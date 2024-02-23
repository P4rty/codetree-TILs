N,K = map(int,input().split())
arr = [0]*(10001)
for _ in range(N):
    a,b = input().split()
    a = int(a)
    if b == "G":
        b = 1
    elif b == "H":
        b = 2
    arr[a] = b
max_photo = 0
for i in range(1,10002-K-1):
    sum_photo = 0
    for j in range(i,i+K+1):
        sum_photo += arr[j]
    max_photo = max(max_photo,sum_photo)
print(max_photo)