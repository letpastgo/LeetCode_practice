class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 0 :
            return 0
        if n == 1 :
            return 1
        
        ways = []
        ways.append(0)
        ways.append(1)
        ways.append(2)
        
        for i in range(3, n+1) :
            ways.append(ways[i-1] + ways[i-2])
        
        return ways[-1]
https://leetcode.com/problems/climbing-stairs/discuss/626562/PYTHON-EVEN-DUMBEST-CAN-UNDERSTAND-99-FAST

https://leetcode.com/problems/climbing-stairs/solution/
