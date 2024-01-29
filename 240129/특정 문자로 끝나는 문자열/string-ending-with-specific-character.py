b = []
for i in range(10):
    a= input()
    b.append(a)
n= input()
cnt=0
for i in range(10):
    if n in b[i][-1]:
        print(b[i])
        cnt+=1
if cnt ==0:
    print('None')