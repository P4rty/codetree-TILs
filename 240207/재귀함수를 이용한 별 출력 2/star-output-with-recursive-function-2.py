n = int(input())
def print_star(n):
    if n ==0 : 
        return
    print("* "*n,end="\n")
    print_star(n-1)
    print("* "*n,end="\n")
print_star(n)