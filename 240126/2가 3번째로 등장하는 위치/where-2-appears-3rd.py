n = int(input())
a = list(map(int,input().split()))
index =0
k=0
for  i in range(n):
    if a[i] == 2:
        index+=1
    if index ==3:
        k=i
        break 
print(k+1)