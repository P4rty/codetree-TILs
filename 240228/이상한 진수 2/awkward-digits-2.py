a = list(input())
n = len(a)
cnt = 0
for i in range(n):
    if cnt == 0 and a[i] == 0 :
        a[i] = 1
        cnt += 1
    elif cnt == n - 1 and a[i] == 1:
        a[i] = 0
dec = 0
for i in range(n-1):
    dec += 2**(n-1-i)

print(dec)