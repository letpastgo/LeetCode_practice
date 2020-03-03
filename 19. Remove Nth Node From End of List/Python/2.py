# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
one-pass alogrithm(actually two pointers)
reference:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/518536/Short-Python-Solution-and-Video-Explanation
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        left = right = head
        
        i = 0
        while(i < n) :
            right = right.next
            i = i + 1
            
        if not right :
            return head.next
        
        while(right.next) :
            left = left.next
            right = right.next
        left.next = left.next.next
        
        return head
