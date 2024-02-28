a = list(input())
n = len(a)
cnt = 0
for i in range(1,n-1):
    if a[i] == 0 and cnt == 0:
        a[i] = 1
        cnt += 1
dec = 0
for i in range(0,n):
    dec += 2**(n-1-i)

print(dec)