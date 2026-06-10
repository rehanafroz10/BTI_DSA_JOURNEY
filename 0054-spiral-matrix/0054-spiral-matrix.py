class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lst=[]
        r = len(matrix)
        c = len(matrix[0])
        t = 0
        l = 0
        ri = c - 1
        bo = r - 1
        while t <= bo and l <= ri:
            for i in range(l, ri + 1):
                lst.append(matrix[t][i])
            t += 1

            for j in range(t, bo + 1):
                lst.append(matrix[j][ri])
            ri -= 1

            if t<=bo:
                for k in range(ri, l - 1, -1):
                    lst.append(matrix[bo][k])
                bo -= 1
            if l<=ri:
                for m in range(bo, t - 1, -1):
                    lst.append(matrix[m][l])
                l += 1

        return lst
