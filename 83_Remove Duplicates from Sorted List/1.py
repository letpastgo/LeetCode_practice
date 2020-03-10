# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None :
            return None
        
        cur = head
        while cur :
            if cur.next == None :
                break
            cur_val = cur.val
            neighbor = cur.next
            if cur_val == neighbor.val :
                while neighbor != None :
                    next_val = neighbor.val
                    if next_val == cur_val :
                        neighbor = neighbor.next
                    else :
                        break
                cur.next = neighbor
            cur = cur.next
        
        
        return head
