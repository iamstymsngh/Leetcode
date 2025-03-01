from typing import List

class Solution:
    # TC - O(nlogn) [for sorting] + O(mlogn) (for each element we call binary search)
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        ans = []
        if len1 < len2:
            nums2.sort()
            for num in set(nums1):
                if num not in ans:
                    if self.search(nums2, num) != -1:
                        ans.append(num)
        else:
            nums1.sort()
            for num in set(nums2):
                if num not in ans:
                    if self.search(nums1, num) != -1:
                        ans.append(num)
        return sorted(ans)[0]