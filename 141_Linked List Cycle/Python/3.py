# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None :
            return False
        
        dicc = {head : 0}
        head = head.next
        cur = head
        
        val = 1
        while(cur) :
            if cur in dicc.keys() :
                return True
            else :
                dicc[cur] = val
                cur = cur.next
            
        return False
        
            
