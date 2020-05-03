
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        cur = head
        listt = []
        while(cur) :
            listt.append(cur.val)
            cur = cur.next
            
        listt.sort()
        listt.reverse()
        
        head = None
        for val in listt :
            if head == None :
                head = ListNode(val)
            else :
                tmp = ListNode(val)
                tmp.next = head
                head = tmp
        
        return head

https://leetcode.com/problems/insertion-sort-list/discuss/510029/python3-97.67-faster-25-less-memory-usage
