n = int(input())

# Please write your code here.

memo = [-1 for _ in range(n+1)]

def dp(n):
    if memo[n] != -1:
        return memo[n]

    if n == 1 or n == 0:
        memo[n] = 1
    elif n == 2:
        memo[n] = 3
    else:
        memo[n] = dp(n - 1) + 2 * dp(n - 2)

    return memo[n]

print(dp(n)%10007)