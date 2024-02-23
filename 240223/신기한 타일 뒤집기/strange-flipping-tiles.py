import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
arr = [0]*200001
idx = 100000
# idx가 1이면 흰색 2면 검은색
for i in range(n):
    n, direction = input().split()
    n = int(n)
    if direction == "L":
        for i in range(idx,idx-n,-1):
            arr[i] = 1
        idx = idx - n + 1
    else:
        for i in range(idx,idx+n):
            arr[i] = 2
        idx = idx + n - 1
cntb = 0
cntw = 0
for i in range(len(arr)):
    if arr[i] == 2:
        cntb += 1
    elif arr[i] == 1:
        cntw += 1
print(cntw,cntb)