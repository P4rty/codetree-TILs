arr1 = []
arr2 = []
a,b = input().split()
for i in range(len(a)):
    if a[i]>='0' and a[i]<='9':
        arr1.append(a[i])
    else:
        break
for i in range(len(b)):
    if b[i]>='0' and b[i]<='9':
        arr2.append(b[i])
    else:
        break
a = ''.join(arr1)
b = ''.join(arr2)
a = int(a)
b = int(b)
print(a+b)