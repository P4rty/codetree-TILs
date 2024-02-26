n = int (input())
arr = list(map(int,input().split()))
cnt = 0
for i in range(n):
    for j in range(i,n):
        avg_min = 0
        length = 0
        for k in range(i,j+1):
            avg_min += arr[k]
            length +=1
        avg_min = avg_min//length
        for k in range(length):
            if avg_min == arr[k]:
                cnt +=1
                break
print(cnt-1)