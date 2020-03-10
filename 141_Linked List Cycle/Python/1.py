# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        while head :
            if head.next == None :
                break
            if head.val == None :
                return True
            else :
                head.val = None
            
            head = head.next
        
        return False
