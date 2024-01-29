a=input()
b=input()
c=input()

an= len(a)
bn= len(b)
cn= len(c)

k = max(an,bn,cn)
l = min(an,bn,cn)
print(k-l)