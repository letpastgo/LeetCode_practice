# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/515452/4-Different-Python-Methods

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        curA = headA
        curB = headB
        
        while(curA != curB) :
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        
        return curA        
