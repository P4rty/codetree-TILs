n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
INF = float('-inf')
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if m[i] > m[j]:
            dp[i] = max(dp[j] + 1, dp[i])

ans = 0
ans = max(dp)

print(ans)