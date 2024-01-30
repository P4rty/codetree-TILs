A = input()
arr = list(A)
check = arr[0]
encoded_result = ''
cnt = 1
for i in range(1,len(arr)):
    if arr[i] != check:
        encoded_result = encoded_result+check+str(cnt)
        check = arr[i]
        cnt = 1
    else:
        cnt += 1
encoded_result = encoded_result + check+str(cnt)

print(len(encoded_result))
print(encoded_result)