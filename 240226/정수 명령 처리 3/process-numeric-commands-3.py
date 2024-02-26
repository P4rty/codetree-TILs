import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
dq = deque()
N = int(input())

for i in range(N):
    q = input()
    if q.startswith('push_front'):
        _, c = q.split(' ')
        dq.appendleft(c)
    if q.startswith('push_back'):
        _, c = q.split(' ')
        dq.append(c)
    if q == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            c = dq.popleft()
            print(c)
    if q == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            c = dq.pop()
            print(c)
    if q == 'size':
        print(len(dq))
    if q == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    if q == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    if q == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])