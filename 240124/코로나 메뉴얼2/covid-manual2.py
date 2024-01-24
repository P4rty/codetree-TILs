ca=0
cb=0
cc=0
cd=0
for _ in range(3):
    a,b = input().split()
    b = int (b)
    if a == 'Y':
        if b>=37:
            ca+=1
        else:
            cc+=1
    elif a== 'N':
        if b>= 37:
            cb+=1
        else:
            cd+=1
if ca>=2:
    print(f'{ca} {cb} {cc} {cd} E')
else:
    print(f'{ca} {cb} {cc} {cd}')