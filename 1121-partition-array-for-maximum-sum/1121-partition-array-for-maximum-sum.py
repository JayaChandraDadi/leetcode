class Solution(object):
    def maxsum(self,i,n,arr,k,dp):
        if i==n:
            return 0
        if dp[i]!=-1:
            return dp[i]
        length = 0
        sum1 = 0
        maxi = float('-inf')
        maximumsum = float('-inf')
        for j in range(i,min(n,i+k)):
            length+=1
            maxi = max(maxi,arr[j])
            sum = 0
            sum1 = length*maxi + self.maxsum(j+1,n,arr,k,dp)
            maximumsum = max(maximumsum,sum1)
        dp[i] = maximumsum
        return dp[i]
    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        dp = [-1]*(n)
        for i in range(n-1,-1,-1):
            length = 0
            sum1 = 0
            maxi = float('-inf')
            maximumsum = float('-inf')
            for j in range(i,min(n,i+k)):
                length+=1
                maxi = max(maxi,arr[j])
                sum = 0
                sum1 = length*maxi + self.maxsum(j+1,n,arr,k,dp)
                maximumsum = max(maximumsum,sum1)
            dp[i] = maximumsum

        return dp[0]
        
        