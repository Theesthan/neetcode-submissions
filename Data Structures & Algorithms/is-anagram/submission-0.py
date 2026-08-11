class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = list(s)
        ts = list(t)
        std = {}
        tsd = {}
        for i in st:
            if i not in std:
                std[i]=1
            else:
                std[i]+=1
        for i in ts:
            if i not in tsd:
                tsd[i]=1
            else:
                tsd[i]+=1
        if std==tsd:
            return True
        return False