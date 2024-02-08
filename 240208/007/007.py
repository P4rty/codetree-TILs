class secret:
    def __init__(self,secret_code,meetingpoint,time):
        self.s = secret_code
        self.m = meetingpoint
        self.t = time
a,b,c = input().split()
secret1 = secret(a,b,c)
print("secret code :",end=" ")
print(secret1.s)
print("meeting point :",end=" ")
print(secret1.m)
print("time :",end=" ")
print(secret1.t)