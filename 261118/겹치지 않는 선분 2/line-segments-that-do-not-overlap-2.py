n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cnt_line = 0

for i in range(n):
    x1, x2 = lines[i]
    is_inter = False
    for j in range(n):
        if i == j:
            continue
        
        x1_prime, x2_prime = lines[j]
        if (x1 < x1_prime and x2 > x2_prime) or (x1 > x1_prime and x2 < x2_prime):
            is_inter = True
            break
    
    if not is_inter:
        cnt_line += 1
    
print(cnt_line)
        

