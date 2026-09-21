class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp = [[[[None]*(2) for _ in range(3)] for _ in range(k)] for _ in range(len(prices)+1)]
        def profit(i,transactions,transactionstype,isrunning):
            if i==len(prices):
                return 0 if isrunning==0 else float('-inf')
            if transactions==k:
                return 0 if isrunning==0 else float('-inf')
            if dp[i][transactions][transactionstype][isrunning]!=None:
                return dp[i][transactions][transactionstype][isrunning]
            if isrunning==0:
                dp[i][transactions][transactionstype][isrunning] = max(-prices[i] + profit(i+1,transactions,1,1),prices[i] + profit(i+1,transactions,2,1),profit(i+1,transactions,0,0))
            else:
                if transactionstype==1:
                    dp[i][transactions][transactionstype][isrunning] = max(prices[i] + profit(i+1,transactions+1,0,0),profit(i+1,transactions,1,1))
                else:
                    dp[i][transactions][transactionstype][isrunning] = max(-prices[i] + profit(i+1,transactions+1,0,0),profit(i+1,transactions,2,1))
            return dp[i][transactions][transactionstype][isrunning]
        return profit(0,0,0,0)