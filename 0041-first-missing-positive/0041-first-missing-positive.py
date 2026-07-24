class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while(i<n):
            if nums[i]==i+1:
                i+=1
            elif nums[i]<=0 or nums[i]>n:
                i+=1
            else:
                idx = nums[i] - 1
                if nums[i]==nums[idx]:
                    i+=1
                    continue
                nums[i],nums[idx] = nums[idx],nums[i]
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1