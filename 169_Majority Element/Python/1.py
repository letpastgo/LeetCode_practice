class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        num = nums[0]
        count = 1
        
        for item in nums[1:] :
            if item != num :
                count -= 1
                if count == 0 :
                    num = item
                    count = 1
            else :
                count += 1
        return num
        
        https://leetcode.com/problems/majority-element/discuss/697300/Python-Very-Simple-and-well-commented-Solution-Based-on-Boyer-Moore's-Algorithm-For-Interviews
