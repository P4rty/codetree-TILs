a = input()
b = input()
exists = False
for i in range(len(a)-len(b)+1):
    cnt = True
    for j in range(len(b)):
        if a[i+j] == b[j]:
            index = i
        if a[i+j] != b[j]:
            cnt = False
    if cnt == True:
        index = i
        break
print(i)