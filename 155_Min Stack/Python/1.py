class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.listt = []
        

    def push(self, x: int) -> None:
        if self.listt :
            self.listt.append( (x, min(x, self.listt[-1][1])) )
        else :
            self.listt.append( (x, x) )
        

    def pop(self) -> None:
        self.listt.pop()

    def top(self) -> int:
        return self.listt[-1][0]

    def getMin(self) -> int:
        return self.listt[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

https://leetcode.com/problems/min-stack/discuss/677394/Simple-Python-3-Solution-O(1)-Time-Complexity-with-One-Liners
