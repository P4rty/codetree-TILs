X, Y = map(int, input().split())

# Please write your code here.
max_num = 0
for i in range(X, Y + 1):
    if i < 10 :
        num = i
    elif 10 <= i <100:
        num = (i % 10) + (i // 10)
    elif 100 <= i <1000:
        num = (i % 10) + ((i // 10) % 10) + (i // 100)
    elif 1000 <= i < 10000:
        num = (i % 10) + ((i // 10) % 10) + ((i // 100) % 10) + (i // 1000)
    elif 10000 <= i < 100000:
        num = (i % 10) + ((i // 10) % 10) + ((i // 100) % 10) + ((i // 1000) % 10) + (i // 10000)
    else:
        num = 1
    
    if num > max_num:
        max_num = num
print(max_num)
