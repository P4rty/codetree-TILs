class Bomb:
    def __init__(self, gowpzhem, color, sec):
        self.gowpzhem = gowpzhem
        self.color = color
        self.sec = sec

Gowpzhem,col,sec = tuple(input().split())
Bomb1 = Bomb(Gowpzhem,col,sec)
print("code : {0}".format(Bomb1.gowpzhem))
print("color : {0}".format(Bomb1.color))
print("second : {0}".format(Bomb1.sec))