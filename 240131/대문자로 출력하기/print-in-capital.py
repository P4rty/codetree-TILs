s = input()
arr = []
for i in range(len(s)):
    if 'A' <= s[i] and  s[i]<= 'Z':
        arr.append(s[i])
    elif 'a' <= s[i] and  s[i]<= 'z':
        a = ord(s[i])-ord('a')+ord('A')
        a = chr(a)
        arr.append(a)
s = ''.join(arr)
print(s)