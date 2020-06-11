class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        start = 0
        end = len(s) - 1
        
        while start < end :
            while not s[start].isalnum() and start < end :
                start += 1
            while not s[end].isalnum() and start < end :
                end -= 1
            if s[start] != s[end] :
                return False
            start += 1
            end -= 1
        return True
        
        https://leetcode.com/problems/valid-palindrome/discuss/672648/Python-two-pointer
