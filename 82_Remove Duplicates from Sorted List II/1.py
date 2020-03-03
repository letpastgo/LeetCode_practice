# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
use dict to record number of items
check the dict to see if repeated item existed
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/525950/Python-using-dictionary
"""

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head :
            return head
        
        dicc = {}
        cur = head
        while(cur) :
            dicc[cur.val] = dicc.get(cur.val , 0) + 1
            cur = cur.next
        
        tmp = cur = ListNode(0)
        cur.next = head
        
        
        while(cur.next) :
            if dicc[cur.next.val] > 1:
                cur.next = cur.next.next
            else :
                cur = cur.next 
                
        return tmp.next
