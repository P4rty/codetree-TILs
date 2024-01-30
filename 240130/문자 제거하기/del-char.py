s = input()
arr = list(s)
while len(arr)>1:
    n= int(input())
    if n >= len(arr):
        arr[(len(arr))-1] = ''
        s = ''.join(arr)
        print(s)
    else:
        arr[n] = ''
        s = ''.join(arr)
        print(s)
    arr = list(s)