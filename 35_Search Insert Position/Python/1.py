class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0 :
            return 0
        elif len(nums) == 1 :
            if target > nums[0] :
                return 1
            else :
                return 0
        
        for idx, val in enumerate(nums) :
            if val == target :
                return idx
            elif val > target :
                return idx
        return len(nums)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = -1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        if nums[mid] < target:
            return mid + 1
        else:
            return mid

https://leetcode.com/problems/search-insert-position/discuss/609258/Python-Simple-Solution-with-Binary-Search





           
