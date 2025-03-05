from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, vote = 0, 0
        for num in nums:
            if vote == 0:
                candidate = num
                vote = 1
            else:
                if num == candidate:
                    vote += 1
                else:
                    vote -= 1

        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        return candidate if count > len(nums)//2 else -1
    