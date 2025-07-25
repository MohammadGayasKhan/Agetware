'''Rajeev has a chart of distinct projected prices for a house over the next several years. He must buy the house in one year and sell it in another, and he must do so at a loss. He wants to minimize her financial loss.
Eg:
price = [20, 15, 7, 2, 13]
His minimum loss is incurred by purchasing in year 2 at price[1] and selling in year 5 at price[4]
Write code that takes as input the number of years and prices for those years and outputs the year to buy and sell in with the loss value'''

import bisect

def find_minimum_loss(prices):
    n = len(prices)
    min_loss = float('inf')
    buy_year = sell_year = -1
    
    # Create a list of (price, year) pairs sorted by price
    price_years = [(price, year) for year, price in enumerate(prices, 1)]
    price_years.sort()  # O(n log n) sort
    
    # Iterate through sorted prices to find consecutive pairs where buy_year > sell_year
    for i in range(1, n):
        current_price, current_year = price_years[i]
        prev_price, prev_year = price_years[i-1]
        
        # Only consider if the buy happens before sell (since we need buy_year < sell_year)
        if prev_year > current_year:
            loss = current_price - prev_price
            if loss < min_loss and loss > 0:
                min_loss = loss
                buy_year = prev_year
                sell_year = current_year
    
    if min_loss == float('inf'):
        return "No valid loss possible"
    return f"Buy in year {buy_year}, Sell in year {sell_year}, Loss = {min_loss}"

if __name__ == "__main__":
    prices = [20, 15, 7, 2, 14]  # Example input
    result = find_minimum_loss(prices)
    print(result)