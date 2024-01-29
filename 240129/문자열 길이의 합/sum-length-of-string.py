n=int(input())

arr=[
    input()
    for _ in range(n)
]
acnt= 0
cnt = 0
for i in range(n):
    cnt+=len(arr[i])
    if 'a' in arr[i][0]:
        acnt+=1
print(f'{cnt} {acnt}')