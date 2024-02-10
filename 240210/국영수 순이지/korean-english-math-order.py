n = int(input())

class Student:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

aclass = []

for _ in range(n):
    name,kor,eng,math = tuple(input().split())
    aclass.append(Student(name,int(kor),int(eng),int(math)))

aclass.sort(key=lambda x:(-x.kor,-x.eng,-x.math))

for i in range(n):
    print("{0} {1} {2} {3}".format(aclass[i].name,aclass[i].kor,aclass[i].eng,aclass[i].math))