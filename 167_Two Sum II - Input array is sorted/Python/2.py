class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two-pointers with "momentum"
        # worst-case O(n), best-case O(logn)
        
        left, right = 0, len(numbers) - 1
        
        while left < right:
            cur = numbers[left] + numbers[right]
            if cur < target:  # need to update left
                i = 0
                while (left + 2**(i+1) < right) and (numbers[left + 2**(i+1)] + numbers[right] < target):
                    i += 1
                left += (2**i)  # always adding at least 1
            elif target < cur:  # need to update right
                i = 0
                while (left < (right - 2**(i+1))) and (numbers[left] + numbers[right - 2**(i+1)] > target):
                    i += 1
                right -= (2**i)  # always decrementing by at least 1
            else:
                return [left + 1, right + 1]
        
        return [-1, -1]  # not found
        
        https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/684286/Python-Two-Pointers-with-%22Momentum%22.-(Best-case%3A-O(logn)-worst-case%3A-O(n))
