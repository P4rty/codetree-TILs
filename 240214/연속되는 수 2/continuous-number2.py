import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)
cnt = 1
fin = []
for i in range(N):
    if arr[i] == arr[i-1]:
        cnt +=1
    if arr[i] != arr[i-1]:
        fin.append(cnt)
        cnt = 1

print(max(fin))