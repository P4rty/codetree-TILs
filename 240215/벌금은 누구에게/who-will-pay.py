import sys
def input():
    return sys.stdin.readline().rstrip()
n,m,k = map(int,input().split())
studentscore = [0]*(n+1)
cnt = 0
for i in range(m):
    s = int(input())
    studentscore[s] += 1
    if studentscore[s] >= k:
        cnt +=1
        print(s)
        break
if cnt == 0 :
    print(-1)