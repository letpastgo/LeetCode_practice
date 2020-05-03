class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2) :
            nums1, nums2 = nums2, nums1
        
        lo = 0
        hi = len(nums1)
        total = len(nums1) + len(nums2) 
        
        while lo <= hi :
            mid1 = (lo + hi) // 2
            left1 = nums1[mid1 - 1] if mid1 != 0 else float('-inf')
            right1 = nums1[mid1] if mid1 != len(nums1) else float('inf')
            
            mid2 = total // 2 - mid1
            left2 = nums2[mid2 - 1] if mid2 != 0 else float('-inf')
            right2 = nums2[mid2] if mid2 != len(nums2) else float('inf')
            
            if left1 <= right2 and left2 <= right1 :
                if total % 2 == 0:
                    return max(left1, left2)/2.0 + min(right1, right2)/2.0
                else:
                    return min(right1, right2)
                
            elif left1 > right2 :
                hi = mid1 - 1
            
            elif left1 < right2 :
                lo = mid1 + 1
        
        return None
 
https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2755/9-lines-O(log(min(mn)))-Python 
