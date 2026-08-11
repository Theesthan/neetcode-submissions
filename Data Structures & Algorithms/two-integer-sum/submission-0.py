class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        init1 = 0
        for i in range(len(nums)):
            if nums[i] not in num:
                num[target-nums[i]]=i
            else:
                return [num[nums[i]], i]
        return []