a,b = map(int,input().split())
arr = [0]*b
while a>1:
    a=a//b
    arr[a%b]+=1 
cnt = 0
for elem in arr:
    cnt += elem*elem
print(cnt)