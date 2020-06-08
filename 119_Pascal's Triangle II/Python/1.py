class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        memory = self.getRow(rowIndex-1)
        for i in range(len(memory)-1, 0, -1):
            memory[i] += memory[i-1]
        return memory + [1]
        
      https://leetcode.com/problems/pascals-triangle-ii/discuss/675743/Python-Recursive-O(k)-Space-%2B-Easy-to-understand
