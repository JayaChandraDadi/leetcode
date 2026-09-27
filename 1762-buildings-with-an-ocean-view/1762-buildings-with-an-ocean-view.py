class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        n = len(heights)
        max1 = float('-inf')
        ans = []
        for i in range(n-1,-1,-1):
            if heights[i]>max1:
                max1 = heights[i]
                ans.append(i)
        return ans[::-1]