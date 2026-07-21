class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i1 = 0
        max_string = 0
        seen_chars = set()

        for i2 in range(len(s)):
            while s[i2] in seen_chars:
                seen_chars.remove(s[i1])
                i1 += 1
            
            seen_chars.add(s[i2])
            max_string = max(max_string, i2 - i1 + 1)
        
        return max_string
