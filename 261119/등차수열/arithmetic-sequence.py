n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
cnt = [0] * 101
for i in range(n - 1):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0:
            k = (a[i] + a[j]) // 2
            cnt[k] += 1

print(max(cnt))
