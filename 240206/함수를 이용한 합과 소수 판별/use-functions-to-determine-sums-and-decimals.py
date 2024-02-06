def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_even(n):
    d = n % 10
    d_10 = n // 10
    if (d + d_10) % 2 == 0:
        return True
    else: 
        return False

a,b = map(int,input().split())
cnt = 0
for i in range(a,b+1):
    if is_prime(i) and is_even(i):
        cnt += 1
print(cnt)