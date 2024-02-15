n,m = map(int,input().split())
arr_a = [0]*1001
arr_b = [0]*1001
distance = 0
time = 0
for _ in range(n):
    d,t = input().split()
    t = int(t) 
    if d == 'L':
        for i in range(time,time+t):
            distance -= 1
            arr_a[i] = distance
        time += t
    else:
        for i in range(time,time+t):
            distance += 1
            arr_a[i] = distance
        time += t
distanceb = 0
time = 0
for i in range(m):
    d,t = input().split()
    t = int(t)
    if d == 'L':
        for i in range(time,time+t):
            distanceb -= 1
            arr_b[i] = distanceb
        time += t
    else:
        for i in range(time,time+t):
            distanceb += 1
            arr_b[i] = distanceb
        time += t


for j in range(time+1):
    if arr_a[j] == arr_b[j]:
        print(j+1)
        break