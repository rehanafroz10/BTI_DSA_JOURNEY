class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        for i in range(0, r):
            for j in range(0, c):
                if i > j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(0, r):
            matrix[i][:] = matrix[i][::-1]
