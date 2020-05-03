class Solution:
    def romanToInt(self, s: str) -> int:
        dicc = {'I' : 1, 'V':5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
        
        
        lenn = len(s)
        if lenn == 1 :
            return dicc[s[0]]
        
        sum = 0
        i = 0
        while(i < lenn - 1) :
            num1 = dicc[s[i]]
            num2 = dicc[s[i + 1]]
            if num1 < num2 :
                sum += (num2 - num1)
                i += 2
            else :
                sum += num1
                i += 1
        if i == lenn - 1 :
            sum += dicc[s[lenn - 1]]
        
        
        return sum
            
