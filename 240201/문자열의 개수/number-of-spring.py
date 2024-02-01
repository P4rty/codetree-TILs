cnt = 0 
arr = []
while True:
    cnt +=1
    s = input()
    if s == '0':
        break
    if cnt % 2 ==1:
        arr.append(s)
print(cnt-1)
for i in range(len(arr)):
    print(arr[i])