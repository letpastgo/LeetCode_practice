# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head == None or head.next == None :
            return False
        
        slow = head
        fast = head.next
        
        #while(1)
        while(fast) :
            if slow == fast :
                return True
            if slow.next != None :
                slow = slow.next
            if fast.next == None :
                return False
            else :
                fast = (fast.next).next
            #else :
            #    if (fast.next).next == None :
            #        return False
            #    else :
            #        fast = (fast.next).next
        
        return False
        
