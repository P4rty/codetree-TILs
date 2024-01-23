n = int(input())
cnt = 0
for i in range(n):
    a,b,c,d = map(int, input().split())
    avg = (a+b+c+d)/4
    if avg >=60:
        print('pass')
        cnt+=1
    else:
        print('fail')
print(cnt)