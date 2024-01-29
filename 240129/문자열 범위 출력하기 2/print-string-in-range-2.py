arr = input()
n = int(input())
if n> len(arr):
    for i in range(-1,-1*len(arr)-1,-1):
        print(arr[i],end="")
else:
    for i in range(-1,-n-1,-1):
        print(arr[i],end="")