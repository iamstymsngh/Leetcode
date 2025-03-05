from collections import Counter

class Solution:
    # TC - O(n)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_counter = Counter(magazine)
        for char in ransomNote:
            if char in mag_counter:
                mag_counter[char] -= 1
                if mag_counter[char] == 0:
                    del mag_counter[char]
            else:
                return False
        return True