s = list(input())
top = 0
for i in range(len(s)):
    if s[i] == '(':
        top += 1
    else:
        top -= 1
        if top < 0:
            print("No")
            exit(0)

if top != 0:
    print("No")
else:
    print("Yes")