n,A = input().split()
n = int(n)
cnt = 0
for i in range(n):
    s = input()
    k = (A == s)
    if k == True:
        cnt+=1
    else:
        pass
print(cnt)