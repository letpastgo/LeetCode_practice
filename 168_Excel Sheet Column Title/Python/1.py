class Solution:
    def convertToTitle(self, n: int) -> str:
        
        strr = ""
        while n > 0:
            strr += chr(65 + (n-1)%26)
            n = (n - 1) // 26
        return strr[::-1]
        
        https://leetcode.com/problems/excel-sheet-column-title/discuss/667480/Python-with-expansion-on-this-question
