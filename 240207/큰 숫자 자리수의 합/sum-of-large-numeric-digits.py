def jari(n):
    if n // 10 == 0:
        return n
    return jari(n//10)+ n%10


a,b,c = map(int,input().split())
mul = a*b*c
print(jari(mul))