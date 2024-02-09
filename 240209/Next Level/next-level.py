class User:
    def __init__(self, name="codetree", lv=10):
        self.name = name
        self.lv = lv
User1 = User()
ID,lev = input().split()
lev = int(lev)
User2 = User(ID,lev)
print("user {0} lv {1}".format(User1.name,User1.lv))
print("user {0} lv {1}".format(User2.name,User2.lv))