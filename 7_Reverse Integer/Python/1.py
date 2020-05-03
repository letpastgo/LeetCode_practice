class Solution:
    def reverse(self, x: int) -> int:
        if(x > 2 ** 31 - 1 or x < -2 ** 31) :
            return 0
        
        if(x < 0):
            tmp = -x
        else :
            tmp = x
        strr = str(tmp)
        strr = strr[::-1]
        
        intt = int(strr)
        if(x > 0) :
            return intt
        else:
            return -intt
          
