class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        else :
            pointer_val = nums[0]
            
        pointer = 0
        for num in nums :
            if num != pointer_val :
                pointer_val = num
                pointer += 1
                nums[pointer] = num
        
        return pointer + 1
https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/594696/Very-fast-Python3-solution-beats-99.1-submissions
