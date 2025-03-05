from typing import List

class Solution:
    # TC - O(n)
    def missingNumber(self, nums: List[int]) -> int:
        n, nset = len(nums), set(nums)
        for i in range(0, n+1):
            if i not in nset:
                return i
