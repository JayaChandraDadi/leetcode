class Solution:
    def merge(self,nums,low,high,mid):
        temp = []
        left = low
        right = mid+1
        while(left<=mid and right<=high):
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while(left<=mid):
            temp.append(nums[left])
            left+=1
        while(right<=high):
            temp.append(nums[right])
            right+=1
        for i in range(len(temp)):
            nums[i+low] = temp[i]
    def mergesort(self,nums,low,high):
        if(low<high):
            mid = (low + high)//2
            self.mergesort(nums,low,mid)
            self.mergesort(nums,mid+1,high)
            self.merge(nums,low,high,mid)
    def sortArray(self, nums: list[int]) -> list[int]:
        self.mergesort(nums,0,len(nums)-1)
        return nums