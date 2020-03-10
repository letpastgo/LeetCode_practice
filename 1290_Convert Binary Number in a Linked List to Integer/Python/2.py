# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getDecimalValue(self, head):
   
        binValue = ""
        
        node = head
        while node:
            if node == None:
                break
            else:    
                binValue += str(node.val)
                node = node.next
        
            
        value = int(binValue, 2)
        
        return value

