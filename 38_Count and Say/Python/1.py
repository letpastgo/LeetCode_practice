class Solution:
    def countAndSay(self, n: int) -> str:
        r = "1"
        for i in range(n-1) :
            r = Solution.count(r)
        return r
        
        
    def count(r : str) -> str :
        
        s = ""
        i = 0
        while i < len(r) :
            start = i
            i += 1
            while i < len(r) and r[i] == r[start] :
                i += 1
            s += (str(i - start) + r[start])
        return s

https://leetcode.com/problems/count-and-say/discuss/606476/Python-3-or-From-Scratch-or-Fast


