class Solution(object):
    def last(self,nums,target):
        index = -1
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]==target:
                index = mid
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return index
    def first(self,nums,target):
        index = -1
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]==target:
                index = mid
                high = mid-1
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return index

    def searchRange(self, nums, target):
        return [self.first(nums,target),self.last(nums,target)]
        