class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        maps = {}
        for i in nums:
            if i not in maps:
                maps[i]=1
            else:
                maps[i]+=1
        for num,freq in maps.items():
            res.append((freq,num))
        res.sort(reverse=True)
        sol=[]
        for i in range(k):
            sol.append(res[i][1])
        return sol