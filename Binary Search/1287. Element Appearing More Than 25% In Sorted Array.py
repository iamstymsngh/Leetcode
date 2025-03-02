from typing import List
from collections import Counter

class Solution:
    # TC - O(n)
    # SC - O(u) where u is the no. of unique elements in arr
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        length = len(arr)
        for key,val in counter.items():
            if val > length / 4:
                return key
                