import sys
def input():
    return sys.stdin.readline().rstrip()

n,m = map(int,input().split())
pos_a = [0]*1000001
pos_b = [0]*1000001
time = 1
for i in range(n):
    t,d = input().split()
    t = int(t)
    for j in range(time,time+t):
        pos_a[j] = pos_a[j-1] +(1 if d == "R" else -1)
    time += t
time = 1
for i in range(m):
    t,d = input().split()
    t = int(t)
    for j in range(time,time+t):
        pos_b[j] = pos_b[j-1] +(1 if d == "R" else -1)
    time +=t

arr = []
direction = 1
cnt = 0
f = []
for k in range(1,time):
    
    if pos_a[k] == pos_b[k] and (pos_a[k] not in f):
        f.append(pos_a[k])
        cnt +=1
print(cnt)