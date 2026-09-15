class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n -1
        while(low<=high):
            mid = (low + high)//2
            if mid-1>=0 and mid+1<n and nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            elif mid-1>=0 and nums[mid-1]>nums[mid]:
                high = mid - 1
            else:
                low = mid + 1