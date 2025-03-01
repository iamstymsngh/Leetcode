# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # TC - O(logn)
    def firstBadVersion(self, n: int) -> int:
        firstBadVersion = n
        low, high = 0, n
        while low <= high:
            mid = low+(high - low)//2
            if isBadVersion(mid):
                firstBadVersion = mid
                high = mid-1
            else:
                low = mid+1
        return firstBadVersion