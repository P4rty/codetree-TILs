s = input()
s2 = input()
arr1 = []
arr2 = []
for i in range(len(s)):
    if s[i] >='0' and s[i] <= '9':
        arr1.append(s[i])

for i in range(len(s2)):
    if s2[i] >='0' and s2[i] <= '9':
        arr2.append(s2[i])
s = ''.join(arr1)
s2 = ''.join(arr2)
s = int(s)
s2 = int(s2)
print(s+s2)