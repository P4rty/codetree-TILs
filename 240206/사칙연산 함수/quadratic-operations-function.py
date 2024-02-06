def tkclrdustks(a,o,c):
    if o == '+':
        print(f'{a} + {c} = {a+c}')
    elif o == '-':
        print(f'{a} - {c} = {a-c}')
    elif o == '/':
        print(f'{a} / {c} = {a//c}')
    elif o == '*':
        print(f'{a} * {c} = {a*c}')
    else:
        print(False)

a, o , c = input().split()
a = int(a)
c = int(c)
tkclrdustks(a,o,c)