start , end= map(int, input().split())
cnt=0
cnt1=0
for i in range(start,end+1 ):
    for j in range(1,i):
        if i%j==0:
            cnt +=1
    if cnt==3:
        cnt1+=1
    cnt=0
print(cnt1)