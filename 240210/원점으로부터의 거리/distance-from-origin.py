class Spot:
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.num = num
spots = []
N = int(input())

for i in range(1,N+1):
    x,y = tuple(input().split())
    spots.append(Spot(int(x),int(y),i))

spots.sort(key = lambda x: abs(x.x)+abs(x.y))

for i in range(N):
    print(spots[i].num)