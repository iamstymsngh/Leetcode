from typing import List
class Solution:
    # TC - O(logn)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)-1
        idx = len(letters)

        while low <= high:
            mid = low+(high - low)//2
            if ord(letters[mid]) > ord(target):
                idx = mid
                high = mid-1
            else:
                low = mid+1
        return letters[idx] if idx != len(letters) else letters[0]
