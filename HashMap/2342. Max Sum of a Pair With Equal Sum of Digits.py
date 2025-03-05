from typing import List
import heapq

class Solution:
    # TC - O(n^2) which fails when constraints are 10^5 range
    # 61 / 84 testcases passed
    def checkIfDigitsEquals(self, val1: int, val2: int) -> bool:
        sum1, sum2 = 0, 0
        while val1 > 0:
            sum1 += val1 % 10
            val1 = val1 // 10

        while val2 > 0:
            sum2 += val2 % 10
            val2 = val2 // 10

        return sum1 == sum2

    def maximumSum(self, nums: List[int]) -> int:
        max_heap = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                # Check for equal sum of digits
                if self.checkIfDigitsEquals(nums[i], nums[j]):
                    heapq.heappush(max_heap, -(nums[i] + nums[j]))
        # print(max_heap)
        if max_heap:
            return -max_heap[0]
        else:
            return -1
