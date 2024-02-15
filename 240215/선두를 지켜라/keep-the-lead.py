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
        pos_a[j] += v
    time +=t



time = 1
for i in range(m):
    v,t = map(int,input().split())
    for j in range(time,time+t):
        pos_b[j] += v
    time +=t
leader_changes = -1
direction_A = 1
direction_B = 1

for k in range(1, time):
    if pos_a[k] > pos_b[k] and direction_A == 1:
        direction_A = -1
        leader_changes += 1
        direction_B = 1
    elif pos_a[k] < pos_b[k] and direction_B == 1:
        direction_B = -1
        leader_changes += 1
        direction_A = 1
print(leader_changes)