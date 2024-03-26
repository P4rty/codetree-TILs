import sys
def input():
    return sys.stdin.readline().rstrip()
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
# n번비교
for i in range(n):
    cnt_row = 1
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1] and cnt_row < m:
            cnt_row += 1
        if arr[i][j] == arr[i][j+1] and cnt_row == m:
            break
        if arr[i][j] != arr[i][j+1] and cnt_row < m:
            cnt_row = 1
        if arr[i][j] != arr[i][j+1] and cnt_row == m:
            break
    if cnt_row >= m:
        cnt += 1
for i in range(n):
    cnt_col = 1
    for j in range(n-1):
        if arr[j][i] == arr[j+1][i] and cnt_col < m:
            cnt_col += 1
        if arr[j][i] == arr[j+1][i] and cnt_col == m:
            break
        if arr[j][i] == arr[j+1][i] and cnt_col < m:
            cnt_col = 1
        if arr[j][i] == arr[j+1][i] and cnt_col == m:
            break
    if cnt_col >= m:
        cnt += 1
print(cnt)