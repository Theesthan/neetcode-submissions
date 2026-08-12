class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        sol = []
        for num,freq in res.most_common(k):
            sol.append(num)
        return sol