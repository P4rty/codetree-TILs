a = input()
cnte = 0
cntb = 0
for i in range(len(a)-1):
    if a[i] == 'e' and a[i+1] == 'e':
        cnte +=1
    if a[i] == 'e' and a[i+1] == 'b':
        cntb +=1
print(f'{cnte} {cntb}')