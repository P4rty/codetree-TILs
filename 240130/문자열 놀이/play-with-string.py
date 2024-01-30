s,q = input().split()
q = int(q)

for i in range(q):
    n,a,b = input().split()
    n = int(n)
    if n == 1:
        a = int(a) - 1
        b = int(b) - 1
        arr = list(s)
        tmp = arr[a]
        arr[a]=arr[b]
        arr[b]=tmp
        s = ''.join(arr)
        print(s)
    if n == 2:
        arr = list(s)
        for i in range( len(arr)):
            if arr[i] == a:
                arr[i] = b
        s = ''.join(arr)
        print(s)