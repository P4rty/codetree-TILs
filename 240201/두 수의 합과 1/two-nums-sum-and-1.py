A,B = map(int,input().split())
s = str(A+B)
cnt = 0
for i in range(len(s)):
    if s[i] == '1':
        cnt += 1
print(cnt)