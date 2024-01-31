s = input()
arr = []
for i in range(len(s)):
    if s[i] <= 'z' and s[i]>= 'a':
        c = chr(ord(s[i]) - ord('a')+ord('A'))
        arr.append(c)
    elif s[i] <= 'Z' and s[i]>= 'A':
        c = chr(ord(s[i]) - ord('A')+ord('a'))
        arr.append(c)
s = ''.join(arr)
print(s)