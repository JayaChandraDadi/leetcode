class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ct = 0
        n = len(nums)
        for i in range(n-1):
            diff = nums[i+1] - nums[i]
            flag = 0
            for j in range(i+2,n):
                if nums[j] - nums[j-1]==diff:
                    ct+=1
                else:
                    break
        return ct