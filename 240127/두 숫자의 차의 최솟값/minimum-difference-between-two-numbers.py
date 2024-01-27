n = int((input()))
arr =list(map(int,input().split()))
ck= arr[0]
mn = 100
for i in arr:
    for j in arr:
        if i < j:
            m=i - j
            m=abs(m)
            mn = min(mn,m)

print(mn)