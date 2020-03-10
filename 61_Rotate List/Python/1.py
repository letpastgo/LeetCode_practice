# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#https://leetcode.com/problems/rotate-list/discuss/531420/Python3-99-100


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if head == None or head.next == None:
            return head
        
        cur = head
        num = 1
        while(cur.next) :
            cur = cur.next
            num += 1
        cur.next = head
                
        steps = k % num
        steps = num - steps
        
        
        i = 0
        cur = head
        while(i < steps):
            cur = cur.next
            i += 1
            
        start = cur
        i = 1
        while(i < num) :
            start = start.next
            i += 1
        start.next = None
        
        return cur
