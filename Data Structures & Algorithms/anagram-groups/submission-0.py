class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        maps = {}
        for i in range(len(strs)):
            if str(sorted(strs[i])) not in maps:
                maps[str(sorted(strs[i]))]=[i]
            else:
                maps[str(sorted(strs[i]))].append(i)
        ind=-1
        for i,lis in maps.items():
            res.append([])
            ind+=1
            for j in lis:
                res[ind].append(strs[j])
        return res
                
            


        