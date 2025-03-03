import math
from typing import List

class Solution:
    # TC - O(nlog max(piles))
    def validEatingSpeed(self, piles: List[int], h: int, eating_speed: int) -> bool:
        time_taken = 0
        for pile in piles:
            time_taken += math.ceil(pile / eating_speed)
        return time_taken <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        eating_speed = max(piles)
        low, high = 1, max(piles)
        while low <= high:
            mid = low + (high - low)//2
            if self.validEatingSpeed(piles, h, mid):
                eating_speed = mid
                high = mid-1
            else:
                low = mid+1
        return eating_speed
