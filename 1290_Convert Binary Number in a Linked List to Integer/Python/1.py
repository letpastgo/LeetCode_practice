# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head.next == None :
            return head.val
        
        import math
        
        left = None
        while(head) :
            right = head.next
            head.next = left
            left = head
            head = right
        
        sum = 0
        num = 0
        cur = left
        while cur :
            sum += int((math.pow(2 , num))) * (cur.val)
            cur = cur.next
            num += 1
            
        return sum
