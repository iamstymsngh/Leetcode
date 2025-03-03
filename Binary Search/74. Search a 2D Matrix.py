from typing import List

class Solution:
    # TC - O(log(r*c))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows*cols-1

        while low <= high:
            mid = low + (high - low)//2
            element = matrix[mid//cols][mid%cols]
            if element == target:
                return True
            elif element < target:
                low = mid+1
            else:
                high = mid-1
        return False
