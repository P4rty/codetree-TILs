a,b = input().split()
if len(a)>len(b):
    print(a,end=" ")
    print(len(a))

elif len(a)<len(b):
    print(b,end=" ")
    print(len(b))

else:
    print('same')