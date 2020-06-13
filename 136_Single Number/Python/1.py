class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicc = {}
        
        for num in nums :
            if num in dicc :
                dicc.pop(num)
            else :
                dicc[num] = 1
        return list(dicc.keys())[0]
        
        https://leetcode.com/problems/single-number/discuss/679229/python-with-80-ms
