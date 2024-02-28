import sys
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

max_coin = 0

for i in range(0,N-2):
    for j in range(0,N-2):
        cnt = 0
        for k in range(i,i+3):
            for l in range(j,j+3):
                if arr[k][l] == 1:
                    cnt += 1
        max_coin = max(max_coin,cnt)
print(max_coin)