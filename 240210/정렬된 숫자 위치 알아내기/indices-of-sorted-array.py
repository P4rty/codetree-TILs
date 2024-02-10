N = int(input())
class Num:
    def __init__(self,val,number,ren):
        self.val =val
        self.number=number
        self.ren = ren
vec = []
a = input().split()
for i in range(N):
    vec.append(Num(int(a[i]),i,i+1))
vec.sort(key=lambda x:x.val)

for i in range(1,N+1):
    vec[i-1].number = i

vec.sort(key=lambda x:x.ren)
for i in range(N):
    print(vec[i].number,end=" ")