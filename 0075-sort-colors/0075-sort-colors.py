class Solution(object):
    def sortColors(self, nums):
        mid = 0
        high = len(nums)-1
        low = 0
        while(mid<=high):
            if nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
        