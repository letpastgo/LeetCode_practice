# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        a = head
        b = []
        
        while(a) :
            b.append(a.val)
            a = a.next
            
        if b == b[: : -1] :
            return True
        else :
            return False
