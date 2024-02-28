import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())

segments = [list(map(int,input().split())) for _ in range(n)]
ans =1000*1000*2

for i in range(n):
    for j in range(i + 1, n):
        if j==n:
            continue
        ans = min(ans,(segments[i][0]-segments[j][0])**2+(segments[i][1]-segments[j][1])**2)

print(ans)