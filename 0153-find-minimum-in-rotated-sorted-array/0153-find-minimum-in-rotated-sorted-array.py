class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        if nums[0]<=nums[n-1]:
            return nums[0]
        low = 0
        high = n-1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[mid+1]<nums[mid]:
                return nums[mid+1]
            if nums[mid]>nums[low]:
                low = mid+1
            else:
                high = mid-1
        return 
