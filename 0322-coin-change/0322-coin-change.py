class Solution(object):
    def count(self,nums,i,target,dp):
        if i==0:
            if target%nums[0]==0:
                return (target/nums[0])
            else:
                return float('inf')
        if dp[i][target]!=-1:
            return dp[i][target]
        nottake = self.count(nums,i-1,target,dp)
        take = float('inf')
        if target>=nums[i]:
            take = 1+self.count(nums,i,target-nums[i],dp)
        dp[i][target] = min(take,nottake)
        return dp[i][target]
    def coinChange(self, coins,amount):
        n = len(coins)
        prev = [0]*(amount+1)
        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i] = i//coins[0]
            else:
                prev[i] = float('inf')
        for i in range(1,n):
            temp = [0]*(amount+1)
            for target in range(amount+1):
                nottake = prev[target]
                take = float('inf')
                if target>=coins[i]:
                    take = 1+temp[target-coins[i]]
                temp[target] = min(take,nottake)
            prev = temp
        if prev[amount]==float('inf'):
            return -1
        else:
            return prev[amount]
        
        