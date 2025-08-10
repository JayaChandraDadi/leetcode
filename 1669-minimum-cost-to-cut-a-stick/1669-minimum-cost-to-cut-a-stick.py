class Solution(object):
    def minimum(self,i,j,arr,dp):
        if i>j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        mini = float('inf')
        for ind in range(i,j+1):
            cost = (arr[j+1] - arr[i-1])+self.minimum(i,ind-1,arr,dp)+self.minimum(ind+1,j,arr,dp)
            mini = min(mini,cost)
        dp[i][j] = mini
        return dp[i][j]
    def minCost(self, n, cuts):
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        length = len(cuts)
        dp = [[0]*(length+2) for _ in range(length+2)]
        for i in range(length-2,0,-1):
            for j in range(i,length-1):
                mini = float('inf')
                for ind in range(i,j+1):
                    cost = (cuts[j+1] - cuts[i-1])+dp[i][ind-1]+dp[ind+1][j]
                    mini = min(mini,cost)
                dp[i][j] = mini
        return dp[1][length-2]