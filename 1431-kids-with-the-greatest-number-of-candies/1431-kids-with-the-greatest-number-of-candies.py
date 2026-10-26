class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n = len(candies)
        maxi = float('-inf')
        result = [False]*n
        for i in range(n):
            maxi = max(maxi,candies[i])
        for i in range(n):
            if extraCandies + candies[i]>=maxi:
                result[i] = True
        return result