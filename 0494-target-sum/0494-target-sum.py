class Solution(object):
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        totalsum = sum(nums)
        t = (totalsum+target)
        if t<0 or t%2!=0:
            return 0
        t = t//2
        prev = [0]*(t+1)
        prev[0] = 1
        if t>=nums[0]:
            prev[nums[0]]+=1
        for i in range(1,n):
            temp = [0]*(t+1)
            temp[0] = 1
            for target in range(t+1):
                notpick = prev[target]
                pick = 0
                if target>=nums[i]:
                    pick = prev[target-nums[i]]
                temp[target] = pick+notpick
            prev = temp
        return prev[t]
        