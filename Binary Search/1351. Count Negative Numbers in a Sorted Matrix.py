from typing import List

class Solution:
    # TC - O(mlogn) where m is the no. of rows
    def searchNegatives(self, rows: List[int]) -> int:
        low, high = 0, len(rows)-1
        ans = 0

        while low <= high:
            mid = low+(high - low)//2
            if rows[mid] < 0:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0
        for row in grid:
            idx = self.searchNegatives(row)
            negatives += (len(row) - idx)
        return negatives
