class Codename():
    def __init__(self,name,score):
        self.name = name
        self.score = score

codenames = []

for _ in range(5):
    name,score = input().split()
    codenames.append(Codename(name,int(score)))
lowest_agent = min(codenames, key= lambda x: x.score)

print(lowest_agent.name, lowest_agent.score)