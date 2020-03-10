
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        dicc = {}
        
        cur = headA
        while(cur) :
            dicc[cur] = cur.next
            cur = cur.next
        cur = headB
        while(cur) :
            if cur in dicc.keys() :
                return cur
            else :
                cur = cur.next
        return None

