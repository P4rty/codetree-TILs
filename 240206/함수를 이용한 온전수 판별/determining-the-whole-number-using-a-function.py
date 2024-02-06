def onjunsoo(n):
    if n % 2 == 0:
        return False
    else:
        if n % 10 == 5:
            return False
        else:
            if n % 3 == 0 and n % 9 != 0:
                return False
            else:
                return True

a,b = map(int, input().split())
cnt = 0
for i in range(a,b+1):
    if onjunsoo(i):
        cnt +=1
print(cnt)