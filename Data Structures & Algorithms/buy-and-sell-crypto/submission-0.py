class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L = 0
        max_profit = 0
        

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
                profit = prices[R] - prices[L]
            if profit > max_profit:
                max_profit = profit
        return max_profit
            

            
        