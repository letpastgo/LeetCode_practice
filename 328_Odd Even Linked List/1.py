# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head is not None :
            oddhead = head
            oddnode = oddhead
            head = head.next
        else :
            return None
        
        if head is not None :
            evenhead = head
            evennode = evenhead
            head = head.next
        else :
            return oddhead
        
        flag = 0
        while head :
            if flag == 0 :
                oddnode.next = head
                oddnode = oddnode.next 
                flag = 1
            else :
                evennode.next = head
                evennode = evennode.next 
                flag = 0
                
            head = head.next
            
        evennode.next = None
        oddnode.next = evenhead
        
        
        return oddhead
