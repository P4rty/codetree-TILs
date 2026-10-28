N = int(input())

# Please write your code here.
memo = [-1 for _ in range(46)]

def febo(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = febo(n - 1) + febo(n - 2)

    return memo[n]
print(febo(N))