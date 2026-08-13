class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        if len(nums)==0:
            return 0
        maxi = 1
        curr = 1
        for i in range(len(nums)-1):
            print(maxi)
            if nums[i]+1==nums[i+1]:
                curr+=1
            elif nums[i]==nums[i+1]:
                continue
            else:
                if curr>maxi:
                    maxi=curr
                curr=1
        return curr if curr>maxi else maxi