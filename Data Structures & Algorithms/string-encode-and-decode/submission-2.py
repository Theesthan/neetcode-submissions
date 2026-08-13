class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+= str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while(i<len(s)):
            j = 0
            while s[i]!='#':
                j=j*10+int(s[i])
                i+=1
            res.append(s[i+1:i+j+1])
            i+=j+1
        return res