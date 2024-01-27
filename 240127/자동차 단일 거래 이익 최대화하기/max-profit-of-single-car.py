def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit

n = int(input())
car_prices = list(map(int, input().split()))

result = max_profit(car_prices)
print(result)