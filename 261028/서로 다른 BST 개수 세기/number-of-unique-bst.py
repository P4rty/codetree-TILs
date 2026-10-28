n = int(input())

# Please write your code here.
memo = [-1 for _ in range(n+1)]

def dp(n):
    if memo[n] != -1:
        return memo[n]

    if n == 1 or n == 0:
        memo[n] = 1
    else:
        memo[n] = 0
        for i in range(n):
            memo[n] += dp(i) *dp(n-1-i)

    return memo[n]

print(dp(n))