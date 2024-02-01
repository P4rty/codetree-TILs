n = int(input())
sm = 0
for i in range(n):
    s = input()
    s= int(s)
    sm = sm + s

sm = str(sm)
sm = sm[1:]+sm[0]
print(sm)