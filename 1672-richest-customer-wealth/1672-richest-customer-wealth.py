class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0]) if m else 0
        maxi = 0
        for i in range(m):
            maxi = max(maxi,sum(accounts[i]))
        return maxi