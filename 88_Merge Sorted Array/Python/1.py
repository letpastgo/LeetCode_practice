class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n >= 1:
            i = n+m-1
			"""
			Compare two arrays one by one each time, put the larger one into the opening from the back to front.
			"""
            if m <= 0 or nums2[n-1] >= nums1[m-1]:
                nums1[i] = nums2[n-1]
                n -= 1
            else:
                nums1[i] = nums1[m-1]
                m -= 1
https://leetcode.com/problems/merge-sorted-array/discuss/501995/Python-3-start-from-the-last-position
