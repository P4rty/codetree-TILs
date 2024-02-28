a = list(input())

n = len(a)
for i in range(n):
    a[i] = int(a[i])

cnt = True
for i in range(n):
    if cnt == True and a[i] == 0 :
        a[i] = 1
        cnt = False
if cnt == True and a[n-1] == 1:
    a[n-1] = 0
elif cnt == True and a[n-1] == 0:
    a[n-1] = 1
dec = 0
for i in range(n):
    dec += 2**(n-1-i)*a[i]

print(dec)