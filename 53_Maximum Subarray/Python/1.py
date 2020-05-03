class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])
        return max(nums)

https://leetcode.com/problems/maximum-subarray/discuss/607083/python3-O(N)

