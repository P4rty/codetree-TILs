import sys

n = int(input())
li = list(map(int,input().split()))
mindistance= sys.maxsize

for i in range(n):
    check = 0
    for j in range(n):
        if i !=j:
            check += li[j]*abs(i-j)
    if check < mindistance:
        mindistance = check
print(mindistance)