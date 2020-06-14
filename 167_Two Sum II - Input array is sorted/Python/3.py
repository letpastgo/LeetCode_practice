class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        no = []
        for i in range(len(numbers)):
            if numbers[i] in no:
                continue
            targ = target - numbers[i]
            low = i+1
            up = len(numbers)-1
            while low<=up:
                mid = (low+up)//2
                # print(low, up, mid)
                if numbers[mid] == targ:
                    return[i+1, mid+1]
                if numbers[mid] > targ:
                    up = mid-1
                if numbers[mid] < targ:
                    low = mid+1
            no.append(numbers[i])
        return
        
        https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/678573/Python-3-solution-using-binary-search.-Beats-87
