n = int(input())

class Student:
    def __init__(self,name,a,b,c):
        self.name =name
        self.a = a
        self.b = b
        self.c = c
aclass = []

for _ in range(n):
    name,a,b,c = tuple(input().split())
    aclass.append(Student(name,int(a),int(b),int(c)))

aclass.sort(key=lambda x: x.a+x.b+x.c)

for student in aclass:
    print(student.name,student.a,student.b,student.c)