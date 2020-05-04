class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if s == "" :
            return 0
        
        i = len(s) - 1
        count = 0
        
        j = i
        while i >= 0 :
            if s[i] == " " :
                i -= 1
            else :
                j = i
                break
                
        while j >= 0 :
            if s[j] != " " :
                count += 1
                j -= 1
            else :
                break
        
        return count
        
https://leetcode.com/problems/length-of-last-word/discuss/610104/python-3
