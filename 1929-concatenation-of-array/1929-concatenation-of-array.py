class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(2*n):
            index = i%n
            ans.append(nums[index])
        return ans