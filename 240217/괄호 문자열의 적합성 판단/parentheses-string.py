s = list(input())
arr = []
for i in range(len(s)):
    if s[i] == '(':
        arr.append(1)
    else:
        if len(arr) != 0 :
            arr.pop()
        else:
            arr.append(2)
            break

if len(arr) != 0:
    print("No")
else:
    print("Yes")