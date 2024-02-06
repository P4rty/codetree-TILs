def printing_star(n):
    if n == 0:
        return
    printing_star(n-1)
    print("*"*n,end="\n")
n= int(input())



printing_star(n)