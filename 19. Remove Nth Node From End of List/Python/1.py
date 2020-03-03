# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
two-pass alogrithm
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        num = 0
        cur = head
        while(cur) :
            num += 1
            cur = cur.next
        if num == n :
            if n == 1 :
                return None
            else :
                return head.next
        
        idx = 1
        cur = head
        dif = num - n
        while(idx < dif) :
            cur = cur.next
            idx += 1
        cur.next = cur.next.next
        
        return head
