class Solution:

    def encode(self, strs: List[str]) -> str:
        sti = ""
        for i in strs:
            sti+= str(len(i)) + "#" + i 
        print(sti)
        return sti
    def decode(self, s: str) -> List[str]:
        strs = list(s)
        res = []
        ind = 0
        while(ind<len(strs)):
            it = 0
            while(strs[ind]!="#"):
                it = it * 10 + int(strs[ind])
                ind+=1
            word=""
            for i in range(it):
                word+=strs[i+ind+1]
            res.append(word)
            ind+=it+1
        return res
