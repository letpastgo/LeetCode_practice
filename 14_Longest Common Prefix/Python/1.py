class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lenn = len(strs)
        if lenn == 0 :
            return ""
        
        minn = 100
        for strr in strs :
            if len(strr) < minn :
                minn = len(strr)
    
        i = 1
        pre = ""
        while(i <= minn) :
            if len(strs[0]) == 0 :
                return ""
            pre = strs[0][0:i]
            
            for strr in strs :
                if len(strr) == 0 :
                    return ""
                com = strr[0:i]
                if pre != com :
                    return strs[0][0:i-1]
            i += 1
        return pre
