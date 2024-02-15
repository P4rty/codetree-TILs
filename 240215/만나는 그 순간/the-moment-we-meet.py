import sys
def input():
    return sys.stdin.readline().rstrip()

n,m = map(int,input().split())
arr_a = []
arr_b = []
distance = 0
time = 0

for _ in range(n):
    d,t = input().split()
    t = int(t) 
    if d == 'L':
        for i in range(time,time+t):
            distance -= 1
            arr_a.append(distance)
        time += t
    else:
        for i in range(time,time+t):
            distance += 1
            arr_a.append(distance)
        time += t
distanceb = 0
time = 0
for i in range(m):
    d,t = input().split()
    t = int(t)
    if d == 'L':
        for i in range(time,time+t):
            distanceb -= 1
            arr_b.append(distanceb)
        time += t
    else:
        for i in range(time,time+t):
            distanceb += 1
            arr_b.append(distanceb)
        time += t

for j in range(time):
    if arr_a[j] == arr_b[j]:
        print(j+1)
        break
    elif j == time-1:
        print(-1)