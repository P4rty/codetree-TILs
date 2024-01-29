a = input()
arr = []
for i in range(1,len(a),2):
    arr.append(a[i])
for i in range(-1,-1*len(arr)-1,-1):
    print(arr[i],end="")