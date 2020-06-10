class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)) :
            profit = max(profit, profit + (prices[i] - prices[i-1]))
        return profit
        
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/664404/Python-Solution-(5-Lines)
