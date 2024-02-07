def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def recursive_lcm(numbers, n):
    if n == 1:
        return numbers[0]
    else:
        return lcm(numbers[n-1], recursive_lcm(numbers, n-1))

n = int(input())
numbers = list(map(int, input().split()))

result = recursive_lcm(numbers, n)
print(result)