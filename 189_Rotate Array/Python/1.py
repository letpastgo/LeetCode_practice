class Solution:
    def gcd(n, k) :
        if n < k :
            n, k = k, n
        
        while k :
            n = n % k
            n, k = k, n
        return n
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        j = 0
        n = len(nums)
        t= nums[0]
        
        if k == 0 :
            return nums
        p = gcd(n, k)
        
        for mod in range(p):
            j = mod
            t = nums[mod]
            for i in range(n// p):
                nums[(j + k) % n], t = t, nums[(j + k) % n]
                j = (j + k) % n
            print(nums)
        return nums
        
        https://leetcode.com/problems/rotate-array/discuss/791464/Python-O(N)-time-O(1)-space-solution-using-GCD
