a = list(input())

n = len(a)
for i in range(n):
    a[i] = int(a[i])

cnt = True
for i in range(n-1):
    if cnt == True and a[i] == 0 :
        a[i] = 1
        cnt = False
if cnt == True and a[n-1] == 1:
    a[n-1] = 0

dec = 0
for i in range(n-1):
    dec += 2**(n-1-i)

if a[n-1] == 1:
    dec+=1

print(dec)