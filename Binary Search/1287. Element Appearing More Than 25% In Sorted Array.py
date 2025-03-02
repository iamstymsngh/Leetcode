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

    # TC - O(n)
    # SC - O(1)
    def findSpecialInteger2(self, arr: List[int]) -> int:
        length = len(arr)
        frequency = length // 4
        for i in range(length - frequency + 1):
            if arr[i] == arr[i+frequency]:
                return arr[i]
                