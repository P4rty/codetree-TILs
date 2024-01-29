A = input()
B = input()
AB = A+B
BA = B+A
AB = list(AB)
BA = list(BA)
cnt =0
for i in range(len(AB)):
    if AB[i] == BA[i]:
        cnt=cnt+1
if cnt == len(AB):
    print("true")
else:
    print("false")