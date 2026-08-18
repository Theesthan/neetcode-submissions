class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = max(prices)
        for p in prices:
            if p<mini:
                mini = p
            else:
                maxi = max(maxi,p-mini)
        return maxi