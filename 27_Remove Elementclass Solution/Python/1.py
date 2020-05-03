class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0 
        while i < len(nums) :
            if nums[i] == val :
                nums.pop(i)
            else :
                i += 1
        return len(nums)        
      
def removeElement(nums, val) -> int:
	i = 0
	l = len(nums)
	c = l
	while i < l:
		if nums[i] == val:
			# shift left
			nums[i:l+1] = nums[i+1:l+1] + [nums[i]]
			c -= 1 # with every shift decrease 1 as val is no longer counted in our list
			l -= 1 # to remove unnecessary iterations
			i -= 1 # to handle cases having consecutive val, like [1,2,2,3], val = 2
		i+=1
https://leetcode.com/problems/remove-element/discuss/604599/Simple-and-Fast-Python3-solution-24ms


