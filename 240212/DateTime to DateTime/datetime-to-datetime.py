a,b,c = map(int,input().split())
d,e,f = 11, 11, 11
elapsed = 0

while True:
    if d == a and e == b and  f == c:

        break
    if f!= c:
        elapsed += 1
        f += 1
    elif e != b:
        elapsed +=60
        e +=1
    
    if f == 60:
        e += 1
        f = 0
    if e == 24:
        d += 1
        e = 0
        f = 0
        
    
print(elapsed)