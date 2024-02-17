from collections import deque

queue = deque()

N,K = map(int,input().split())
for i in range(1,N+1):
    queue.append(i)
while len(queue) !=0:
    for i in range(K):
        a = queue.popleft()
        queue.append(a)
    print(queue.pop(),end= " ")