class Solution:
    def firstoccurance(self,nums,low,high,target):
        low = 0
        high = len(nums)-1
        ans = -1
        while(low<=high):
            mid = (low + high)//2
            if nums[mid]==target:
                ans = mid
                high = mid-1
            elif nums[mid]>target:
                high = mid - 1
            else:
                low = mid + 1
        return ans
    def lastoccurance(self,nums,low,high,target):
        low = 0
        high = len(nums)-1
        ans = -1
        while(low<=high):
            mid = (low + high)//2
            if nums[mid]==target:
                ans = mid
                low = mid + 1
            elif nums[mid]>target:
                high = mid - 1
            else:
                low = mid + 1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.firstoccurance(nums,0,len(nums)-1,target),self.lastoccurance(nums,0,len(nums)-1,target)]
