class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxsum = float('-inf')
        j = k
        i = 0
        best_i = float('-inf')
        for j in range(k,n):
            best_i = max(best_i,nums[i])
            maxsum = max(maxsum,best_i + nums[j])
            i+=1
        return maxsum