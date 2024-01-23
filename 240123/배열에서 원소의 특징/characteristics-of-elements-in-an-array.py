a = list(map(int,input().split()))
b= 0
for element in a:
    if a[element] % 3 ==0:
        b= element
        break
print(b)