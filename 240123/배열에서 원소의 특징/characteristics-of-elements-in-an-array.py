a = list(map(int, input().split()))
b = 0

for i in range(len(a)):
    if a[i] % 3 == 0:
        b = i - 1
        break
print(a[b])