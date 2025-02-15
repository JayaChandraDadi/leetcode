class Solution(object):
    def binsearch(self,nums,low,high,target):
        if low>high:
            return -1
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        elif target>nums[mid]:
            return self.binsearch(nums,mid+1,high,target)
        else:
            return self.binsearch(nums,low,mid-1,target)
    def search(self, nums, target):
        return self.binsearch(nums,0,len(nums)-1,target)
    
        