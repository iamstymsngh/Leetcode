class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, length, start = 0, 0, 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            if right - left + 1 > length:
                start = left
                length = right - left + 1

        longest_substring = s[start:start+length]
        print(f"substring : {longest_substring}")
        return length