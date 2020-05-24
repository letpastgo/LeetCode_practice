class Solution:
    def mySqrt(self, x: int) -> int:
        
        low = 0.0
        high = x
        
        for _ in range(64) :
            mid = (low + high) / 2
            if mid*mid > x :
                high = mid
            else :
                low = mid
        
        return int(mid)
https://leetcode.com/problems/sqrtx/discuss/617293/Python-Binary-Search.

