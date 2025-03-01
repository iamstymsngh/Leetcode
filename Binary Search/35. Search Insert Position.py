from typing import List

class Solution:
    # TC - O(logn)
    # Lower bound - find first index of the target if it were inserted in the array
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        ans = len(nums)

        while low <= high:
            mid = low+(high - low)//2
            if nums[mid] >= target:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans