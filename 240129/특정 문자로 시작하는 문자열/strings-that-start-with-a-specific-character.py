n = int(input())
arr= []
for i in range(n):
    a= input()
    arr.append(a)

ch = input()
lg = 0
cnt = 0
for i in range(n):
    if ch == arr[i][0]:
        cnt+=1
        lg += len(arr[i])
if cnt != 0:
    print("{0} {1:.2f}".format(cnt,lg/cnt))