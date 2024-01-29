n= int(input())
arr = list(input().split())
brr="".join(arr)
for i in range(len(brr)):
    print(brr[i],end="")
    if i%5==4:
        print()