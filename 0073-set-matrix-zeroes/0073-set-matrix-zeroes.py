class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        
        row_track = [0 for _ in range(r)]
        col_track = [0 for _ in range(c)]

        # 1. Mark the rows and columns that contain a 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_track[i] = -1  # Fixed: index into the row
                    col_track[j] = -1  # Fixed: index into the column

        # 2. Update the matrix based on the tracking lists
        for i in range(r):
            for j in range(c):
                # Fixed: check col_track[j] instead of the whole variable
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0