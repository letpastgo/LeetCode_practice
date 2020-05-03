class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        res = [""]*numRows
        flag = True
        index = 0
        
        if(numRows == 1) :
            return s
        
        for ch in s:
            if flag:
                res[index] += ch
                if index == numRows - 1 :
                    flag = False
                    index -= 1
                else :
                    index += 1
            else :
                res[index] += ch
                if index == 0 :
                    index += 1
                    flag = True
                else:
                    index -= 1
        return "".join(res)
        
https://leetcode.com/problems/zigzag-conversion/discuss/556787/Python3-solution
