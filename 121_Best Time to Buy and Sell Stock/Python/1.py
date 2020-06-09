class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 :
            return 0
        profit = 0
        pre = prices[-1]
        
        for i in range(len(prices) - 2, -1, -1) :
            if prices[i] < pre :
                if (pre - prices[i]) > profit :
                    profit = (pre - prices[i])
            else :
                pre = prices[i]
        return profit
        
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/678121/Python-Simple-and-Understandable-Solution
