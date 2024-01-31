s,q = input().split()
q = int(q)
for i in range(q):
    n = int(input())
    if n == 1:
        s = s[1:]+s[0]
        print(s)
    elif n==2:
        s = s[-1]+s[:-1]
        print(s)
    elif n==3:
        s = s[::-1]
        print(s)