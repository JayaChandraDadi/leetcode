class Solution:
    def ceil(self,nums,target):
        low = 0
        high = len(nums)
        while(low<=high):
            mid = (low + high)//2
            if nums[mid]<target:
                low = mid + 1
            else:
                high = mid - 1
        return low
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = []
        n = len(nums)
        for i in range(n):
            if not temp or temp[-1]<nums[i]:
                temp.append(nums[i])
            else:
                index = self.ceil(temp,nums[i])
                temp[index] = nums[i]
        return len(temp)