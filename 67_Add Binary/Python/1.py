class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        if len(b) > len(a) :
            a, b = b, a
        aa = list(a)
        bb = list(b)
        a_len = len(aa)
        b_len = len(bb)
        
        add_list = [0 for i in range(a_len - b_len)]
        bb = add_list + bb
        
        cc = []
        i = a_len - 1
        plus = 0
        while i >=0 :
            tmp = int(bb[i]) + int(aa[i]) + plus
            if tmp >= 2:
                tmp -= 2
                plus =1
            else :
                plus = 0
            cc.insert(0, tmp)
            i -= 1
        if plus == 1 :
            cc.insert(0, 1)
        
        return "".join('%s' %item for item in cc)
            
