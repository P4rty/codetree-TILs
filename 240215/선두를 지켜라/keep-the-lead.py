import sys
def input():
    return sys.stdin.readline().rstrip()

n,m = map(int,input().split())
pos_a = [0]*1000001
pos_b = [0]*1000001
time = 1
for i in range(n):
    v,t = map(int,input().split())
    for j in range(time,time+t):
        pos_a[i] += v
    time +=t



time = 1
for i in range(m):
    v,t = map(int,input().split())
    for j in range(time,time+t):
        pos_b[i] += v
    time +=t
arr = []
direction = 1
for k in range(1,time+1):
    if pos_a[k] > pos_b[k]:
        direction = 1
        arr.append(direction)
    elif pos_a[k] < pos_b[k]:
        direction = -1
        arr.append(direction)
    elif pos_a[k] == pos_b[k]:
        direction == 0
        arr.append(direction)
cnt = 0
for k in range(1,len(arr)):
    if arr[k] != arr[k-1] and arr[k] != 0 :
        cnt+=1
print(cnt)