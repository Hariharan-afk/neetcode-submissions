class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            i = (bottom + top) // 2
            left = 0
            right = len(matrix[0]) - 1
            if matrix[i][0] <= target <= matrix[i][-1]:
                while left<=right:
                    j = (right + left) // 2
                    if matrix[i][j] == target:
                        return True
                    elif matrix[i][j] < target:
                        left = j + 1
                    else:
                        right = j - 1
                return False
            elif matrix[i][-1] < target:
                top = i + 1
            else:
                bottom = i - 1
        return False

        
        