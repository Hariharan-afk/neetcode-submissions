class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        i = 1
        while i < len(prices):
            sell_price = prices[i]
            if prices[i-1] < buy_price:
                buy_price = prices[i-1]
            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit
            i+=1
        return max_profit


        