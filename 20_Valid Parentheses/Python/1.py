class Solution:
    def isValid(self, s: str) -> bool:
        
        
        dicc = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        
        for ch in s :
            if not stack :
                if ch in dicc :
                    stack.append(ch)
                else :
                    return False
            else :
                if ch in dicc :
                    stack.append(ch)
                elif ch != dicc[stack[-1]] :
                    return False
                else :
                    stack.pop()
        if stack :
            return False
        return True

https://leetcode.com/problems/valid-parentheses/discuss/595529/Python-Using-Stack-O(N)
