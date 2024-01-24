a = list(map(int,input().split()))
cnt = [0]*10
for elem in a:
    if elem //10 != 0:
        elem = elem//10
        cnt[elem-1] +=1
for i in range(9,-1,-1):
    print(f'{i*10+10} - {cnt[i]}')