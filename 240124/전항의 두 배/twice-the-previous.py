a1,a2 = map(int,input().split())
a = []
a.append(a1)
a.append(a2)
for i in range(2,10):
    a.append(a[i-1]+2*a[i-2])
for i in range(10):
    print(a[i],end=" ")