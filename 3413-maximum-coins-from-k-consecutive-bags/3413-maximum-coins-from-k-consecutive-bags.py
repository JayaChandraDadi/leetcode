class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        n = len(coins)
        prefix = [0]*(n+1)
        for i in range(n):
            l = coins[i][0]
            r = coins[i][1]
            c = coins[i][2]
            sum1 = c*(r-l+1)
            prefix[i+1] = sum1 + prefix[i]
        def left_ceil(coins,k):
            ans = n
            low = 0
            high  = n-1
            while(low<=high):
                mid = (low + high)//2
                if coins[mid][1]>=k:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
        def right_ceil(coins,k):
            ans = -1
            low = 0
            high = n - 1
            while(low<=high):
                mid = (low + high)//2
                if coins[mid][0]<=k:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        def find(l,r):
            left_index = left_ceil(coins,l)
            right_index = right_ceil(coins,r)
            if left_index==right_index:
                left_overlap = max(l,coins[left_index][0])
                right_overlap = min(r,coins[left_index][1])
                return (right_overlap - left_overlap+1)*coins[left_index][2]
            else:
                left_overlap = max(l,coins[left_index][0])
                right_overlap = min(r,coins[left_index][1])
                leftsum = (right_overlap - left_overlap+1)*coins[left_index][2]
                left_overlap = max(l,coins[right_index][0])
                right_overlap = min(r,coins[right_index][1])
                rightsum = (right_overlap - left_overlap+1)*coins[right_index][2]
                mid_sum = prefix[right_index] - prefix[left_index + 1]
                return leftsum + rightsum + mid_sum
        
        max_coins = 0
        for l, r, c in coins:
            max_coins = max(
                max_coins,
                find(l, l + k - 1)
            )
            max_coins = max(
                max_coins,
                find(r - k + 1, r)
            )

        return max_coins