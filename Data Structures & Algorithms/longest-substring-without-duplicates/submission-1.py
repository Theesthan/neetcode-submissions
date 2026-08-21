class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxi = 0
        maps = {}
        for r in range(len(s)):
            if s[r] in maps:
                l = max(l,maps[s[r]] + 1)
            maps[s[r]]=r
            maxi = max(maxi,r - l + 1)
        return maxi
