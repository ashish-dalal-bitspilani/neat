# Time complexity : O(n)
# Space complexity : O(1)

def max_profit(prices: list[int])-> int:
    profit, min_price = 0, max(prices)

    for price in prices:
        if price < min_price:
            min_price = price
        profit = max(profit, price-min_price)

    return profit

print("==================================")
print(max_profit(prices = [10,1,5,6,7,1]))
print(max_profit(prices = [10,8,7,5,2]))
print("==================================")

# Time complexity : O(n)
# Space complexity : O(1)

def maximum_profit(prices: list[int])-> int:
    highest_profit, left = 0, 0

    for right in range(1,len(prices)):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            highest_profit = max(profit, highest_profit)
        else:
            left = right

    return highest_profit

print("==================================")
print(max_profit(prices = [10,1,5,6,7,1]))
print(max_profit(prices = [10,8,7,5,2]))
print("==================================")