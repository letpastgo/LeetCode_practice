# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#https://leetcode.com/problems/swap-nodes-in-pairs/discuss/529841/python-faster-than-97.82



class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None :
            return head
        
        dum = ListNode(0)
        dum.next = head
        
        cur = dum
        
        while(cur.next) :
            if(not cur.next.next) :
                return dum.next
            n1 = cur.next
            n2 = cur.next.next
            n3 = cur.next.next.next
            cur.next = n2
            n2.next = n1
            n1.next = n3
            cur = cur.next.next
            
        return dum.next
            
