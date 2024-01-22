n= int(input())
cnt = ord('A')
for i in range(1,n+1):
    for k in range(i-1):
        print(" ",end=" ")
    for j in range(n-i+1):
        print(chr(cnt),end=" ")
        cnt+=1
        if cnt > ord('Z'):
            cnt = ord('A')
    print()