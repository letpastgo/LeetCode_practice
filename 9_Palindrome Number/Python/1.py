class Solution:
    def isPalindrome(self, x: int) -> bool:
        strr = str(x)
        lenn = len(strr)
        if lenn == 1:
            return True
        
        midd = int(lenn/2)
        if lenn % 2 == 0 :
            mid1 = midd
            mid2 = midd - 1
        else :
            mid1 = midd + 1
            mid2 = midd - 1

        if(strr[0 : mid1] == strr[-1 : mid2 : -1]) :
            return True
        else :
            return False
