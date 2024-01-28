n,m = map(int,input().split())
li_b= []
li_a = []
for i in range(n):
    li_t=list(map(int,input().split()))
    li_b.append(li_t)
for i in range(n):
    li_t=list(map(int,input().split()))
    li_a.append(li_t)

for k in range(n):
    for l in range(m):
        if li_b[k][l] == li_a[k][l]:
            print(0,end=" ")
        else :
            print(1,end=" ")
    print()