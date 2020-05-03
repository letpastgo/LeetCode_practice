class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        for i in range(len(strs[0])):
            temp = strs[0][i]
            for ele in strs[1:]:
                if len(ele) < i+1 or ele[i] != temp: return strs[0][:i]
        return strs[0]
https://leetcode.com/problems/longest-common-prefix/discuss/595669/Python3-70-Short-Easy-understand
