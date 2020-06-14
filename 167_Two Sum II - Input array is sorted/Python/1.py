class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        indexs = []
        for i in range(len(numbers)) :
            diff = target - numbers[i]
            if diff in numbers[i : len(numbers)] :
                for j in range(i + 1, len(numbers)) :
                    if numbers[j] == diff :
                        indexs.append(i + 1)
                        indexs.append(j + 1)
                        break
            if len(indexs) == 2 :
                return indexs
