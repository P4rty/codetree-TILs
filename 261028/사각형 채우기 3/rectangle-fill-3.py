n = int(input())

# Please write your code here.
memo = [-1 for _ in range(n+1)]

def dp(n):
    if memo[n] != -1:
        return memo[n]
    if n == 1:
        memo[n] = 2
    elif n == 2:
        memo[n] = 7
    elif n == 0:
        memo[n] = 1
    else:
        memo[n] = 3 * dp(n-1) + dp(n-2) - dp(n-3)
    
    return memo[n]


answer = dp(n) % 1000000007

print(answer)