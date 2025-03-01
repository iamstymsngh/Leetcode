from typing import List

class Solution:
    # Brute Force
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        for num in nums:
            if num == 0:
                continue
            elif num < 0:
                neg += 1
            else:
                pos += 1

        return max(pos, neg)