def flflf(N):
    k = 0
    for i in range(1,N+1):
        k = k +i
    return k//10

N = int(input())
print(flflf(N))