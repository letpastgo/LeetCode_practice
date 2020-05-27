class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        listt = [ [1], [1, 1] ]
        if numRows == 0 :
            return []
        elif numRows == 1:
            return [ [1] ]
        elif numRows == 2 :
            return listt
        for i in range(numRows - 2) :
            num = len(listt[-1])
            new_list = []
            new_list.append(1)
            for j in range(num - 1) :
                new_list.append( (listt[-1][j] + listt[-1][j + 1]) )
            new_list.append(1)
            listt.append(new_list)
        return listt
