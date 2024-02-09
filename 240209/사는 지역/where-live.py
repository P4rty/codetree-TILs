class Living:
    def __init__(self, name, num, legion):
        self.name = name
        self.num = num
        self.legion = legion
        
users = []
n = int(input())
for _ in range(n):
    name, num, legion = input().split()

    users.append(Living(name,num,legion))

slowest_person = max(users, key=lambda x: x.name)
   
print("name {0}".format(slowest_person.name))
print("addr {0}".format(slowest_person.num))
print("city {0}".format(slowest_person.legion))