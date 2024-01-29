arr=["apple", "banana", "grape", "blueberry", "orange"]
word = input()
cnt=0
for i in range(5):
    for j in range(2,4):
        if word == arr[i][j]:
            print(arr[i])
            cnt+=1
print(cnt)