class Solution:
    def isPalindrome(self, s: str) -> bool:
        o = ""
        for i in s:
            if i.isalnum():
                o+= i.lower()
            else:
                continue
        r = o[::-1]
        return r==o