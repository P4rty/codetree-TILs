N = int(input())
x,y = 0,0
for _ in range(N):
    s,n = input().split()
    n = int(n)
    if s =='N':
        y += n
    elif s == 'W':
        x -= n
    elif s == 'S':
        y -= n
    elif s == 'E':
        x += n
print(x,y)