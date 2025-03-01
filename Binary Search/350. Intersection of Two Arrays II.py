import collections
from typing import List

class Solution:
    #  TC - O(nlogn) [for sorting] + O(mlogn) (for each element we call binary search)
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

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1, len2 = len(nums1), len(nums2)
        map1, map2 = collections.Counter(nums1), collections.Counter(nums2)
        ans = []
        if len1 < len2:
            nums2.sort()
            for num in set(nums1):
                if num not in ans:
                    if self.search(nums2, num) != -1:
                        get_min_count = min(map1[num], map2[num])
                        ans.extend([num] * get_min_count)
        else:
            nums1.sort()
            for num in set(nums2):
                if num not in ans:
                    if self.search(nums1, num) != -1:
                        get_min_count = min(map1[num], map2[num])
                        ans.extend([num] * get_min_count)
        return ans
