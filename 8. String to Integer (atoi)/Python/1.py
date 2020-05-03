class Solution:
    def myAtoi(self, s: str) -> int:
        
        if(len(s) == 0) :
            return 0
        
        for i, val in enumerate(s) :
            if val != ' ' :
                s = s[i:]
                break
        if(len(s) == 0) :
            return 0
        
        if s[0] != '+' and s[0] != '-' and  s[0].isdigit() == False :
            return 0
        
        sign = 1
        if s[0] == '+' :
            s = s[1:]
        elif s[0] == '-' :
            sign = -1
            s = s[1:]
            
        if(len(s) == 0) :
            return 0
        
        for i, val in enumerate(s) :
            if val.isdigit() == False :
                s = s[:i]
                break
        if(len(s) == 0) :
            return 0
        
        if sign == 1 :
            if int(s,10)>=2**31-1:
                return 2**31-1
        else :
            if int(s,10)>=2**31:
                return -(2**31)
        return sign*int(s,10)

https://leetcode.com/problems/string-to-integer-atoi/discuss/583839/Easy-to-understand-in-Python-using-slicing-and-isdigit
