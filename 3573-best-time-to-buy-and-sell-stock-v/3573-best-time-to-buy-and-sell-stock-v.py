class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        dp = [[[[None] * 2 for _ in range(3)]
               for _ in range(k)]
              for _ in range(n)]

        def profit(i, transactions, transactionstype, isrunning):
            if i == n:
                return 0 if isrunning == 0 else float('-inf')

            if transactions == k:
                return 0 if isrunning == 0 else float('-inf')

            if dp[i][transactions][transactionstype][isrunning] is not None:
                return dp[i][transactions][transactionstype][isrunning]

            if isrunning == 0:

                # 1 = normal transaction
                # 2 = short transaction
                # 0 = no transaction
                ans = max(
                    -prices[i] + profit(i + 1, transactions, 1, 1),
                    prices[i] + profit(i + 1, transactions, 2, 1),
                    profit(i + 1, transactions, 0, 0)
                )

            elif transactionstype == 1:

                # sell normal position or continue holding
                ans = max(
                    prices[i] + profit(
                        i + 1, transactions + 1, 0, 0
                    ),
                    profit(i + 1, transactions, 1, 1)
                )

            else:

                # buy back short position or continue holding
                ans = max(
                    -prices[i] + profit(
                        i + 1, transactions + 1, 0, 0
                    ),
                    profit(i + 1, transactions, 2, 1)
                )

            dp[i][transactions][transactionstype][isrunning] = ans
            return ans

        return profit(0, 0, 0, 0)