import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)
cnt = 1
fma = 0
for i in range(N):
    if arr[i] == arr[i-1]:
        cnt +=1
    if arr[i] != arr[i-1]:
        if cnt > fma :
            fma = cnt
        cnt = 1
print(fma)