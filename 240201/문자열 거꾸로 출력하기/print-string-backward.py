while True:
    s = input()
    if s == 'END':
        break
    for i in range(-1,-1*len(s)-1,-1):
        print(s[i],end="")
    print()