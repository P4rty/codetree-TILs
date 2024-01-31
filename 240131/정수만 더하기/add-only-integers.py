s = input()
arr = []
for i in range(len(s)):
    if s[i] <= '9' and s[i]>= '0':
        arr.append(s[i])
sm = 0
for i in range(len(arr)):
    sm +=int(arr[i])
print(sm)