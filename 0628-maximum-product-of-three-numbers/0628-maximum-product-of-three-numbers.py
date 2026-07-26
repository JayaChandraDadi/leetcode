class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        maximum = nums[-1]
        secondmax = nums[-2]
        thirdmax = nums[-3]
        minimum = nums[0]
        secondmin = nums[1]
        return max(maximum*secondmax*thirdmax,maximum*minimum*secondmin)