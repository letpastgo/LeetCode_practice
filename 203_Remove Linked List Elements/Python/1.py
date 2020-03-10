# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        cur = head
        pre = None
        
        while(cur) :
            if cur.val == val :
                if pre == None :
                    head = head.next
                    cur = head
                else :
                    pre.next = cur.next
                    cur = cur.next
            else :
                pre = cur
                cur = cur.next
        
        return head
        
