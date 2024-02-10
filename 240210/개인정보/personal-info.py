class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
people = []
for _ in range(5):
    name,height,weight = tuple(input().split())
    people.append(Person(name,int(height),float(weight)))
print("name")
people.sort(key=lambda x: (x.name))
for i in range(5):
    print(people[i].name, people[i].height,people[i].weight)

print()
people.sort(key=lambda x: (-x.height))
print("height")
for i in range(5):
    print(people[i].name, people[i].height,people[i].weight)