a,b = input().split()
arr = list(a)
brr = list(b)
brr[0:2]=arr[0:2]
b=''.join(brr)  
print(b)