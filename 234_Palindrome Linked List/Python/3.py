#https://leetcode.com/problems/palindrome-linked-list/discuss/533277/Python3-solution-easy-to-understand

class Solution: # O(n), O(n)
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        return tmp == tmp[::-1]
