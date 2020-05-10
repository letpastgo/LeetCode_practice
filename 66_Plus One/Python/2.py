class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lenn = len(digits)
        
        i = lenn-1
        plus = 1
        while i >= 0 :
            tmp = digits[i] + plus 
            digits[i] = tmp % 10
            plus = tmp // 10
            if plus == 0 :
                break
            i -= 1
        if plus == 1 :
            digits.insert(0, plus)
        return digits


        number = 0
        
        for i in range(len(digits)):
			# first part handles multiple of 10 based on digit location, second part handles digit
            number += (10 ** i) * (digits[~i])
        return [d for d in str(number+1)]
https://leetcode.com/problems/plus-one/discuss/613096/Python-solution-O(n)
