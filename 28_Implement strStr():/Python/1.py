class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        len_all = len(haystack)
        len_sub = len(needle)
        if len_all < len_sub :
            return -1
        
        times = len_all - len_sub + 1
        i = 0
        
        while i < times :
            if haystack[i:i+len_sub] == needle :
                return i
            i += 1
        return -1
