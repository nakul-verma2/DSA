prices=[7,1,5,3,6,4]
def check(prices):
    min_price = float('inf') # Start with a very high number
    max_profit = 0
    
    for price in prices:
        # 1. Update the lowest price found so far
        if price < min_price:
            min_price = price
        
        # 2. Calculate profit if we sold at the current price
        current_profit = price - min_price
        
        # 3. Update max_profit if this deal is better
        if current_profit > max_profit:
            max_profit = current_profit
    print(max_profit)
check(prices)