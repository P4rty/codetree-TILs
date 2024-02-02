def count_numbers(a, b):
    count = 0
    
    for num in range(a, b + 1):
        if '3' in str(num) or '6' in str(num) or '9' in str(num) or num % 3 == 0:
            count += 1
            
    return count

a,b = map(int,input().split())
print(count_numbers(a,b))