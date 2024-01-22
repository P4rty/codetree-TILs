n= int(input())
cnt = ord('A')
for i in range(1,n+1):
    for j in range(i):
        print(chr(cnt),end="")
        cnt+=1
        if cnt > ord('Z'):
            cnt = ord('A')
    print()