n = int(input())

class Student:
    def __init__(self,height,weight,number):
        self.height = height
        self.weight = weight
        self.number = number
aclass = []

for i in range(1,n+1):
    height,weight = tuple(input().split())
    aclass.append(Student(int(height),int(weight),int(i)))

aclass.sort(key=lambda x: (x.height,-x.weight,x.number))

for i in range(n):
    print(aclass[i].height,aclass[i].weight,aclass[i].number)