# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(head) :
        left = None
        while head:
            right = head.next
            head.next = left
            left = head
            head = right
        return left
            
        
    def find_mid(head) :
        slow = fast = head
        while(fast and fast.next) :
            fast = fast.next.next
            slow = slow.next
        
        return slow.next if fast else slow
        
        
    
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None :
            return True
        
        mid = Solution.reverse(Solution.find_mid(head))
        
        while(mid):
            if mid.val != head.val :
                return False
            else :
                head , mid = head.next , mid.next
        return True
