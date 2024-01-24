a = list(map(int,input().split()))
cnt = [0]*10
for elem in a:
    elem = elem//10
    cnt[elem-1] +=1

for i in range(10,0,-1):
    print(f'{i*10} - {cnt[i-1]}')