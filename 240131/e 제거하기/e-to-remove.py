s = input()
arr = list(s)
k = s.index('e')
arr = arr[:k]+arr[k+1:]
s = ''.join(arr)
print(s)