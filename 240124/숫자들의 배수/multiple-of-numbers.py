n=int(input())
i=1
cnt =0
while True:
    a = n*i
    print(a,end=" ")
    i+=1
    if a%5 ==0:
        cnt+=1
    if cnt ==2:
        break