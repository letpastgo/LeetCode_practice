class Solution:
def lengthOfLastWord(self, s: str) -> int:

    if ' ' in s.strip()[::-1]:
        return s.strip()[::-1].index(' ')
    
    return len(s.strip())
    
    https://leetcode.com/problems/length-of-last-word/discuss/603943/Python3-solution
