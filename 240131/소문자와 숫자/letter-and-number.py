s = input()
arr = []
for i in range(len(s)):
    if s[i] <= '9' and s[i]>= '0':
        arr.append(s[i])
    elif s[i] <= 'z' and s[i]>= 'a':
        arr.append(s[i])
    elif s[i] <= 'Z' and s[i]>= 'A':
        c = chr(ord(s[i]) - ord('A')+ord('a'))
        arr.append(c)
s = ''.join(arr)
print(s)