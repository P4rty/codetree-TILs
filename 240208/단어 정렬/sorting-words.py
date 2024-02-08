n = int(input())
a = []
for _ in range(n):
    s = input()
    a.append(s)
a = sorted(a)
for i in range(n):
    print(a[i])