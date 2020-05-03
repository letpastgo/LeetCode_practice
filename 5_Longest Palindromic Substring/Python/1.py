class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if(s == ''):
            return s
        
        i = 0
        res = []
        while i < len(s):
            left = i
            right = i
            cur = s[i]
            flag = False
            while (left - 1) >= 0 or (right + 1) < len(s)  :
                if not flag:
                    if (left -1) >= 0 :
                        if(s[left-1] == s[i]):
                            cur = s[left-1] + cur
                            left -= 1
                            continue
                    if right + 1 < len(s) :
                        if(s[right + 1] == s[i]):
                            cur = cur + s[right + 1]
                            right += 1
                            continue
                flag = True
                
                left -= 1
                right += 1
                if left >= 0 and right < len(s):
                    if(s[left] == s[right]):
                        cur = s[left] + cur + s[right]
                    else:
                        break
                else :
                    break
            if cur not in res :
                res.append(cur)
            i += 1
            
        res.sort(key = len, reverse = True)
        return res[0]
     
https://leetcode.com/problems/longest-palindromic-substring/discuss/566416/Python-93-newbies-friendly-solution-(with-comments)

